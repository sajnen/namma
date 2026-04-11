import csv
import json
import sys
from pathlib import Path

INPUT_FILE = Path('places.json')
OUTPUT_FILE = Path('places.csv')

HEADERS = [
    'place',
    'latitude',
    'longitude',
    'status',
    'seating',
    'flooring',
    'camera_surveillance',
    'signage',
    'roof',
    'continuous_pathway',
    'wheelchair_entryway',
    'access_blocked',
    'tactile_pathway',
    'cleanliness',
]


def to_safe_string(value):
    if value is None:
        return ''
    return str(value)


def convert_json_to_csv(source_path: Path, target_path: Path):
    with source_path.open('r', encoding='utf-8') as f:
        places = json.load(f)

    rows = []
    for item in places:
        desc = item.get('description', {}) or {}
        facilities = desc.get('facilities', {}) or {}
        accessibility = desc.get('accessibility', {}) or {}

        rows.append({
            'place': to_safe_string(item.get('place')),
            'latitude': to_safe_string(item.get('latitude')),
            'longitude': to_safe_string(item.get('longitude')),
            'status': to_safe_string(desc.get('status')),
            'seating': to_safe_string(facilities.get('seating')),
            'flooring': to_safe_string(facilities.get('flooring')),
            'camera_surveillance': to_safe_string(facilities.get('camera_surveillance')),
            'signage': to_safe_string(facilities.get('signage')),
            'roof': to_safe_string(facilities.get('roof')),
            'continuous_pathway': to_safe_string(facilities.get('continuous_pathway')),
            'wheelchair_entryway': to_safe_string(accessibility.get('wheelchair_entryway')),
            'access_blocked': to_safe_string(accessibility.get('access_blocked')),
            'tactile_pathway': to_safe_string(accessibility.get('tactile_pathway')),
            'cleanliness': to_safe_string(desc.get('cleanliness')),
        })

    with target_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else INPUT_FILE
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else OUTPUT_FILE

    if not src.exists():
        print(f'Error: source file not found: {src}')
        sys.exit(1)

    total = convert_json_to_csv(src, dst)
    print(f'Wrote {dst} with {total} rows from {src}')


if __name__ == '__main__':
    main()
