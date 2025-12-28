#!/usr/bin/env node

/**
 * One-command publish helper:
 * - sync homepage_index.md -> _index.md
 * - git add -A
 * - git commit -m "..."
 * - git push
 *
 * NOTE: GitHub Pages still requires a push to trigger deployment.
 * This script just removes the "manual steps" friction.
 */

const { execSync } = require("node:child_process");

function sh(cmd) {
  return execSync(cmd, { stdio: "inherit" });
}

function shOut(cmd) {
  return execSync(cmd, { encoding: "utf8" }).trim();
}

const args = process.argv.slice(2);
const msgIdx = args.findIndex((a) => a === "-m" || a === "--message");
const message =
  msgIdx >= 0 && args[msgIdx + 1]
    ? args[msgIdx + 1]
    : `site update ${new Date().toISOString().slice(0, 16).replace("T", " ")}`;

try {
  // Ensure homepage mirror is updated
  sh("node scripts/sync_homepage.js");

  // Stage changes
  sh("git add -A");

  // If nothing to commit, exit cleanly
  const status = shOut("git status --porcelain");
  if (!status) {
    console.log("No changes to commit.");
    process.exit(0);
  }

  // Commit + push
  sh(`git commit -m "${message.replace(/\"/g, '\\"')}"`);
  sh("git push");
} catch (e) {
  process.exit(1);
}


