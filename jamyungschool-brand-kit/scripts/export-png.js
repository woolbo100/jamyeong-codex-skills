const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const root = path.resolve(__dirname, "..");
const assetDir = path.join(root, "assets");
const pngDir = path.join(root, "png");
fs.mkdirSync(pngDir, { recursive: true });

const files = fs.readdirSync(assetDir).filter((file) => file.endsWith(".svg"));

async function main() {
  for (const file of files) {
    const input = path.join(assetDir, file);
    const output = path.join(pngDir, file.replace(/\.svg$/i, ".png"));
    await sharp(input, { density: 180 })
      .png()
      .toFile(output);
  }

  const visual = path.join(assetDir, "13-representative-visual.png");
  if (fs.existsSync(visual)) {
    fs.copyFileSync(visual, path.join(pngDir, "13-representative-visual.png"));
  }

  console.log(`Exported ${files.length} PNG files to ${pngDir}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
