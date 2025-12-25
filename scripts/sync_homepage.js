#!/usr/bin/env node

/**
 * Sync homepage_index.md to _index.md
 * This script automatically copies content from homepage_index.md to _index.md
 * so you only need to edit homepage_index.md
 */

const fs = require('fs');
const path = require('path');

const sourceFile = path.join(__dirname, '..', 'content', 'english', 'homepage_index.md');
const targetFile = path.join(__dirname, '..', 'content', 'english', '_index.md');

function syncHomepage() {
  try {
    // Check if source file exists
    if (!fs.existsSync(sourceFile)) {
      console.error(`Error: ${sourceFile} not found!`);
      process.exit(1);
    }

    // Read source file
    const content = fs.readFileSync(sourceFile, 'utf8');
    
    // Write to target file
    fs.writeFileSync(targetFile, content, 'utf8');
    
    console.log('✅ Successfully synced homepage_index.md to _index.md');
  } catch (error) {
    console.error('❌ Error syncing homepage:', error.message);
    process.exit(1);
  }
}

// Run sync
syncHomepage();

