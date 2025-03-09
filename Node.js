.name: LOCK4
{
  "query": "incompatibles con mi proyecto",
  "scopingQuery": "repo:kevin-4444/Kelvin"
}Muerte instantánea para los q no van con mí proyecto==
  push:
    tags:
      - 'v*.*.*'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'

      - name: Install dependencies
        run: npm install

      - name: Build project
        run: npm run build

      - name: Create Release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false

      - name: Upload Release Asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: path/to/build/output
          asset_name: output.zip
          asset_content_type: application/zip
git add .github/workflows/release.yml
git commit -m "Add GitHub Actions workflow for release"
git push origin main
git tag v1.0.0
git push origin v1.0.0