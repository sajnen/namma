# Google Sheets Integration Setup Guide

## Complete Setup Instructions

### Step 1: Create a Google Sheet

1. Go to [sheets.google.com](https://sheets.google.com)
2. Click **"+ Create"** → **"Blank spreadsheet"**
3. Name it: **"Namma Nildana Survey"**
4. In cell A1, add these headers in row 1:
   ```
   A1: Timestamp
   B1: Email
   C1: Phone
   D1: Feedback
   ```

### Step 2: Create Google Apps Script

1. Open your Google Sheet
2. Click **Extensions** → **Apps Script**
3. A new tab will open
4. **Delete** any existing code
5. **Paste this code:**

```javascript
function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    // Add row to sheet
    sheet.appendRow([
      new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }),
      data.email,
      data.phone || '',
      data.feedback
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({success: true}))
      .setMimeType(ContentService.MimeType.JSON);
  } catch(e) {
    return ContentService
      .createTextOutput(JSON.stringify({success: false, error: e.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

### Step 3: Deploy as Web App

1. In Apps Script editor, click **"Deploy"** → **"New deployment"**
2. Click the **gear icon** → Select **"Web app"**
3. Set these options:
   - **Execute as:** Select your Google account
   - **Who has access:** "Anyone"
4. Click **"Deploy"**
5. **Important:** Copy the **Deployment URL** (looks like this):
   ```
   https://script.googleapis.com/macros/d/ABCDEF123456/usercontent
   ```

### Step 4: Add URL to Your Code

1. Open `script.js` in your project
2. Find this line at the top:
   ```javascript
   const GOOGLE_SHEETS_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';
   ```
3. **Replace** with your actual URL:
   ```javascript
   const GOOGLE_SHEETS_URL = 'https://script.googleapis.com/macros/d/ABCDEF123456/usercontent';
   ```

---

## Testing Locally

### Method 1: Python Server (Simplest)

```bash
cd c:\Users\sajit\OneDrive\Documents\GitHub\namma
python -m http.server 8000
```

Visit: `http://localhost:8000/map.html`

**Test the survey:**
1. Click "Feedback" button
2. Fill in:
   - Email: `test@example.com`
   - Phone: `+91 98765 43210`
   - Feedback: `Test message`
3. Click "Submit Feedback"
4. Check your Google Sheet for the response

### Method 2: Netlify CLI

```bash
npm install -g netlify-cli
cd your-project-path
netlify dev
```

Visit: `http://localhost:8888/map.html`

---

## Troubleshooting

### Issue: "Please fill in all required fields"
- ✅ Make sure email and feedback are filled
- ✅ Phone is optional

### Issue: "Survey is not configured yet"
- ✅ You forgot to add the Google Apps Script URL to `script.js`
- ✅ Replace `'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE'` with your actual URL

### Issue: Form submits but data doesn't appear in Sheet
- ✅ Check that Apps Script deployment shows **"Anyone"** access
- ✅ Make sure the **URL in script.js matches** your deployment URL
- ✅ Check browser console for errors (F12 → Console tab)

### Issue: Deployment URL returns 403 error
- ✅ The URL needs to be **updated** each time you redeploy Apps Script
- ✅ Click "Deploy" → "New deployment" (not "Update")

### Issue: No data appears in Sheet
- ✅ Check that column headers are in Row 1
- ✅ Verify Apps Script code was pasted correctly
- ✅ Try submitting again

---

## Viewing Survey Responses

### In Google Sheet
- Open your **"Namma Nildana Survey"** sheet
- Each response appears as a new row
- Data includes: Timestamp, Email, Phone, Feedback

### Export as CSV
1. Click **File** → **Download** → **Comma Separated Values (.csv)**
2. Opens in Excel or any spreadsheet app

### Export as PDF
1. Click **File** → **Download** → **PDF Document**

---

## Deploying to Netlify

The code works the same on Netlify as locally!

```bash
# 1. Push to GitHub
git add .
git commit -m "Add Google Sheets survey"
git push

# 2. Deploy to Netlify
netlify deploy --prod
```

Or connect GitHub to Netlify for automatic deployments.

---

## Security Notes

- ✅ Google Apps Script is public-facing (safe - it only receives POST data)
- ✅ Anyone can submit to your sheet (feature, not a bug)
- ✅ No sensitive data in the URL
- ✅ Google handles all security

---

## What You Can Do Now

✅ Test locally with Python server
✅ Test on Netlify after deployment  
✅ Responses auto-save to Google Sheets
✅ Export data as CSV anytime
✅ Share sheet with collaborators
✅ Set up automatic notifications for new responses

---

## Next Steps

1. **Create Google Sheet** (Step 1)
2. **Create Apps Script** (Step 2)
3. **Deploy as Web App** (Step 3)
4. **Add URL to script.js** (Step 4)
5. **Test locally** with Python server
6. **Deploy to Netlify** when ready

**Estimated time:** 5-10 minutes

---

## Video Alternative

If you prefer video, Google Sheets + Apps Script tutorials are available on YouTube by searching "Google Apps Script Web App POST data"

---

Need help? Check the troubleshooting section above or deploy and test!
