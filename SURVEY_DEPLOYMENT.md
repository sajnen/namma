# Survey Feature - Netlify Deployment Guide

## Overview
The survey feature has been implemented with the following components:
- Survey modal popup with email, phone (optional), and feedback fields
- Local storage-based data persistence (works with Netlify static hosting)
- Export functionality for manual data download
- Responsive design for all devices

## File Structure
```
namma/
├── map.html                 (Contains survey modal HTML)
├── styles.css              (Contains survey modal styles)
├── script.js               (Contains survey logic)
├── survey-responses.json   (Initial template data file)
└── netlify.toml            (Netlify configuration - optional)
```

## How It Works

### 1. Survey Modal (map.html)
- "Feedback" button in the map header opens the survey
- Modal overlays the map with form fields
- Close button (X) or clicking overlay closes it

### 2. Data Storage Options for Netlify

#### Option A: Local Storage (Current - No Backend Needed)
- Survey responses are saved in browser's localStorage
- Works completely on Netlify static hosting (no backend required)
- Data persists across browser sessions
- Users can manually export data using `exportSurveyData()` function

#### Option B: Netlify Forms (Recommended)
- Update form in map.html to use Netlify Forms:
  ```html
  <form id="surveyForm" name="survey" method="POST" netlify>
    <!-- fields remain same -->
  </form>
  ```
- Netlify automatically collects submissions at: yoursite.netlify.com/admin/forms/survey
- Data appears in Netlify dashboard

#### Option C: Netlify Functions + Fauna/Supabase Database
- Use serverless functions to save to external database
- More advanced setup for persistent backend storage

## Deployment Steps

### 1. Local Testing
```bash
# Test locally with live server or Python server
cd your-project-directory

# Python 3
python -m http.server 8000

# Or use VS Code Live Server extension
```
Visit: `http://localhost:8000/map.html`

### 2. Prepare for Netlify

**Option A: Local Storage (Current Setup)**
No additional setup needed. Just deploy as-is.

**Option B: Switch to Netlify Forms** (Recommended)
1. Update form in map.html with `name="survey"` and `netlify` attribute
2. The form structure is already compatible

### 3. Deploy to Netlify

**Method 1: Netlify CLI**
```bash
npm install -g netlify-cli

netlify deploy --prod
```

**Method 2: Git Integration**
1. Push to GitHub/GitLab
2. Go to netlify.com → New site → Import existing project
3. Select repository
4. Build settings: (leave default for static sites)
5. Deploy

**Method 3: Drag & Drop**
1. Go to netlify.com
2. Drag and drop your project folder
3. Automatic deployment

### 4. Enable Netlify Forms (Optional)
If switching to Netlify Forms:
1. Update form in map.html
2. Redeploy
3. Access responses at: yoursite.netlify.app/admin/forms/survey

## Accessing Survey Data

### Local Storage (Current)
In browser console:
```javascript
// View all responses
JSON.parse(localStorage.getItem('surveys'))

// Export to JSON
exportSurveyData()
```

### Manual Export
- Click "Feedback" → Fill form → Submit
- Browser downloads JSON file with all responses
- Format: `survey-responses-YYYY-MM-DD.json`

### Netlify Forms Dashboard
- Log in to Netlify
- Go to Site settings → Forms
- View and download submissions

## Survey Data Format

### JSON Structure
```json
{
  "metadata": {
    "project": "Namma Nildana",
    "description": "Bus Stop Accessibility Survey",
    "exportDate": "2026-04-22T10:30:00Z",
    "totalResponses": 1
  },
  "responses": [
    {
      "email": "user@example.com",
      "phone": "+91 98765 43210",
      "feedback": "User feedback text here...",
      "timestamp": "2026-04-22T10:30:00Z",
      "busStopVisited": null
    }
  ]
}
```

## Features

✅ Email validation (required)
✅ Phone number support (optional)
✅ Feedback textarea (required)
✅ Local storage persistence
✅ Export to JSON
✅ Modal animations
✅ Mobile responsive
✅ Accessible form (ARIA labels)
✅ Close button and cancel button
✅ Form validation

## Recommended Setup

For production with Netlify:

1. **Use Netlify Forms** (simplest)
   - Pros: Built-in, managed by Netlify, dashboard access, spam protection optional
   - Cons: No real-time analytics

2. **Use Local Storage** (current)
   - Pros: No backend needed, users can export anytime
   - Cons: Data lost if user clears browser data

3. **Use External Service** (future)
   - Firebase, Supabase, or backend API
   - More complex setup but persistent cloud storage

## Files Modified

1. **map.html**
   - Added survey modal HTML structure
   - Added "Feedback" button to header

2. **styles.css**
   - Added comprehensive survey modal styling
   - Added animations and responsive design
   - Added mobile-friendly layout

3. **script.js**
   - Added `initSurveyModal()` function
   - Added `saveSurveyResponse()` for localStorage
   - Added `exportSurveyData()` for manual export

4. **survey-responses.json** (New)
   - Template file showing expected data format
   - Can be included in repo for reference

## Testing Checklist

- [ ] Open survey on map page
- [ ] Test email validation (try submitting without email)
- [ ] Test feedback validation (try submitting without feedback)
- [ ] Phone number is optional (submit with empty phone)
- [ ] Submit valid form
- [ ] Close modal with X button
- [ ] Close modal with Cancel button
- [ ] Close modal by clicking overlay
- [ ] Export survey data
- [ ] Test on mobile (responsive)
- [ ] Test in different browsers

## Troubleshooting

**Survey button doesn't appear:**
- Check that map.html has the "Feedback" button
- Verify styles.css is loaded

**Form doesn't submit:**
- Check browser console for errors
- Verify JavaScript is enabled
- Check that all required fields are filled

**Data not saving:**
- Check localStorage quota (usually 5-10MB)
- Verify browser allows localStorage
- Check browser console for errors

**Export not working:**
- Verify responses exist in localStorage
- Check browser download settings
- Try different browser

## Next Steps

1. Test locally with `http://localhost:8000/map.html`
2. Click "Feedback" button to open survey
3. Submit a test response
4. Export data using browser console or export function
5. Deploy to Netlify
6. Monitor responses in your preferred method

---

**Need help?** Contact support or check Netlify documentation at docs.netlify.com
