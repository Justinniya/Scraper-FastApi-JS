const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const userDataDir = '/home/berting/.config/google-chrome'; // Your Chrome profile base dir
  const profileDir = 'Profile 8';

  const context = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    args: [
      `--profile-directory=${profileDir}`,
      '--disable-blink-features=AutomationControlled'
    ],
  });

  const page = await context.newPage();
  await page.goto('https://airbnb.com');

  // Wait to ensure cookies are set (optional)
  await page.waitForTimeout(50000);

  // Get cookies
  const cookies = await context.cookies();

  // Save cookies to cookies.json
  fs.writeFileSync('airbnb_listing.json', JSON.stringify(cookies, null, 2));

  console.log('Cookies saved to cookies.json');

  // Close if desired
  // await context.close();
await page.waitForTimeout(5000);
})();
