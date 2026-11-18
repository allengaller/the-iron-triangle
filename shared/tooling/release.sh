#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
ROOT="$REPO/books/the-bte-book"
BUILD="$REPO/shared/tooling"
DIST="$REPO/shared/dist"
VERSION="v1.0"
STAGE="$DIST/bte-book-$VERSION"
ZIP="$DIST/bte-book-$VERSION.zip"

"$BUILD/build.sh"

rm -rf "$STAGE" "$ZIP"
mkdir -p "$STAGE"

cp "$DIST/bte-book.html" "$STAGE/"
cp "$DIST/bte-book.epub" "$STAGE/"
cp "$DIST/bte-book.pdf" "$STAGE/"
cp "$BUILD/cover.png" "$STAGE/"
cp "$BUILD/metadata.yaml" "$STAGE/"
cp "$REPO/shared/review/the-bte-book/release-readme.md" "$STAGE/README.md"
cp "$ROOT/CHANGELOG.md" "$STAGE/"
cp "$REPO/shared/review/the-bte-book/release-v1.0.md" "$STAGE/"
cp "$REPO/LICENSE" "$STAGE/LICENSE"

( cd "$DIST" && zip -qr "$(basename "$ZIP")" "$(basename "$STAGE")" )

echo "Release ready:"
ls -lh "$ZIP"
echo "Contents:"
ls -lh "$STAGE"