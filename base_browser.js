const { chromium } = require('playwright');
const { main } = require('./facebook_post');

async function main_browser(){
  const browser = await chromium.launch({
    headless: false,
    args: [
      '--no-sandbox',
      '--disable-blink-features=AutomationControlled',
    ],
  });

  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    viewport: { width: 1420, height: 975 },
    deviceScaleFactor: 1,
    isMobile: false,
    hasTouch: false,
    locale: 'en-PH',
    timezoneId: 'Asia/Manila',
    geolocation: { latitude: 14.5995, longitude: 120.9842 },
    permissions: ['geolocation'],
  });

  // 🛡️ Manual stealth tweaks
  await context.addInitScript(() => {
    // Remove webdriver property
    Object.defineProperty(navigator, 'webdriver', { get: () => false });

    // Mock plugins
    Object.defineProperty(navigator, 'plugins', {
      get: () => [1, 2, 3, 4, 5],
    });

    // Mock languages
    Object.defineProperty(navigator, 'languages', {
      get: () => ['en-PH', 'en'],
    });

    // Mock Chrome object
    window.chrome = { runtime: {} };
  });

  const page = await context.newPage();
  return page;

  // 💡 You can now perform your automation safely
};

module.exports = main_browser;
