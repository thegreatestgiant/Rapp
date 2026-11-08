const fs = require('fs');
const path = require('path');

/**
 * Calculates academic metadata (season, academic year, testTarget)
 * based on the class schedule and the Rebbi's halachic observation:
 * 
 * - Fall Semester:
 *   - Midterms end in late October.
 *   - On the 1st Sunday of November, Daylight Saving Time ends (clocks fall back 1 hr).
 *   - Mincha Gedola shifts earlier (~12:20 PM), so davening Mincha in class begins
 *     before class dismissal at 1:00 PM.
 *   - Starting on the 1st Sunday in November -> 'Final'.
 * 
 * - Spring Semester:
 *   - Begins late January / early February.
 *   - Mincha Gedola is ~12:30 PM, so Mincha is davened in class before 1:00 PM.
 *   - On the 2nd Sunday of March, Daylight Saving Time begins (clocks spring forward 1 hr).
 *   - Mincha Gedola shifts after 1:00 PM (~1:30 PM), so they STOP davening Mincha in class.
 *   - Midterms coincide with this transition; starting on the 2nd Sunday in March -> 'Final'.
 *
 * @param {Object} [config] Optional config object (defaults to loading config.json)
 * @param {Date|string} [targetDate] Optional date (defaults to current date)
 * @returns {{ season: string, year: string, testTarget: string }}
 */
function getAcademicMetadata(config, targetDate) {
  if (!config) {
    try {
      const configPath = path.resolve(__dirname, '..', 'config.json');
      if (fs.existsSync(configPath)) {
        config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
      }
    } catch (e) {
      config = {};
    }
  }
  config = config || {};

  const explicitTarget = config.default_test_target || config.test_target;

  let now;
  if (targetDate) {
    if (typeof targetDate === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(targetDate)) {
      const [y, m, d] = targetDate.split('-').map(Number);
      now = new Date(y, m - 1, d);
    } else {
      now = new Date(targetDate);
    }
  } else {
    now = new Date();
  }

  const month = now.getMonth() + 1; // 1-12
  const day = now.getDate();
  let year = now.getFullYear();
  let season, testTarget;

  // Mid-January cutoff for previous Fall final
  if (month === 1 && day < 15) {
    season = 'Fall';
    year = year - 1;
    testTarget = explicitTarget || 'Final';
  } else if (month < 6 || (month === 6 && day < 15)) {
    season = 'Spring';
    // Spring Semester: DST starts on 2nd Sunday in March (clocks forward 1hr).
    // Mincha Gedola shifts from ~12:30 PM to ~1:30 PM (after 1:00 PM class ends),
    // so davening Mincha in class STOPS. This marks the end of midterms and transition to Finals.
    const firstSunMarch = 1 + (7 - new Date(year, 2, 1).getDay()) % 7;
    const secondSunMarch = firstSunMarch + 7;
    const autoTarget = (month < 3 || (month === 3 && day < secondSunMarch)) ? 'Midterm' : 'Final';
    testTarget = explicitTarget || autoTarget;
  } else {
    season = 'Fall';
    // Fall Semester: DST ends on 1st Sunday in November (clocks back 1hr).
    // Mincha Gedola shifts from ~1:25 PM to ~12:20 PM (before 1:00 PM class ends),
    // so davening Mincha in class BEGINS. This marks the end of midterms and transition to Finals.
    const firstSunNov = 1 + (7 - new Date(year, 10, 1).getDay()) % 7;
    const autoTarget = (month < 11 || (month === 11 && day < firstSunNov)) ? 'Midterm' : 'Final';
    testTarget = explicitTarget || autoTarget;
  }

  return { season, year: String(year), testTarget };
}

// Support CLI execution: node academic_metadata.js [optional YYYY-MM-DD]
if (require.main === module) {
  const argDate = process.argv[2] || undefined;
  const result = getAcademicMetadata(null, argDate);
  console.log(JSON.stringify(result));
}

module.exports = { getAcademicMetadata };
