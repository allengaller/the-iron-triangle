#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
ROOT="$REPO/books/the-bte-book"
BUILD="$REPO/shared/tooling"
DIST="$REPO/shared/dist"
mkdir -p "$DIST"

if [ ! -f "$BUILD/cover.png" ]; then
  echo "Generating cover..."
  (cd "$BUILD" && python3 -I "$BUILD/make_cover.py")
fi

SHARED="$REPO/shared"
FILES=(
  "$ROOT/front-matter.md"
  "$SHARED/00-copyright-and-license.md"
  "$SHARED/00-commitment-chain.md"
  "$SHARED/00-disclaimer-and-anonymization.md"
  "$SHARED/00-citation.md"
  "$SHARED/00-reading-status.md"
  "$ROOT/front-reading-guide.md"
  "$ROOT/ch01-bte-origin-evolution.md"
  "$ROOT/ch02-triangle-boundary.md"
  "$ROOT/ch03-value-proposition.md"
  "$ROOT/ch04-ai-era-redefined.md"
  "$ROOT/ch05-opportunity-judgment.md"
  "$ROOT/ch05-practical.md"
  "$ROOT/ch06-customer-decision-insight.md"
  "$ROOT/ch06-practical.md"
  "$ROOT/ch07-value-engineering.md"
  "$ROOT/ch07-practical.md"
  "$ROOT/ch08-technical-credibility-proof.md"
  "$ROOT/ch08-practical.md"
  "$ROOT/ch09-commercial-architecture.md"
  "$ROOT/ch09-practical.md"
  "$ROOT/ch10-negotiation-relationship.md"
  "$ROOT/ch10-practical.md"
  "$ROOT/ch11-lead-qualification.md"
  "$ROOT/ch12-requirements-scenarios.md"
  "$ROOT/ch13-value-case.md"
  "$ROOT/ch14-solution-shaping.md"
  "$ROOT/ch15-poc-proof.md"
  "$ROOT/ch16-bidding-proposal.md"
  "$ROOT/ch17-negotiation-signing.md"
  "$ROOT/ch18-handover-expansion.md"
  "$ROOT/ch19-financial-procurement.md"
  "$ROOT/ch20-large-deal-governance.md"
  "$ROOT/ch21-case-studies.md"
  "$ROOT/ch22-selling-ai-solutions.md"
  "$ROOT/ch23-ai-for-bte.md"
  "$ROOT/ch23-bte-copilot-tutorial.md"
  "$ROOT/ch24-ai-era-commitment-trust.md"
  "$ROOT/ch25-bte-irreplaceability.md"
  "$ROOT/ch26-bte-measurement.md"
  "$ROOT/ch27-bte-maturity.md"
  "$ROOT/ch28-career-team.md"
  "$ROOT/ch28-team-building-practical.md"
  "$ROOT/appx-a-glossary.md"
  "$ROOT/appx-b-opportunity-process.md"
  "$ROOT/appx-c-methodology-mapping.md"
  "$ROOT/appx-d-further-reading.md"
  "$ROOT/appx-e-contribution-guide.md"
  "$ROOT/appx-f-financial-procurement-compliance.md"
  "$ROOT/appx-g-bte-evaluation-standard.md"
  "$ROOT/back-epilogue.md"
)

RESOURCE_PATH="$ROOT:$ROOT/../the-tam-book:$ROOT/../the-sa-book:$SHARED"

echo "Building HTML..."
pandoc "${FILES[@]}" \
  --metadata-file="$BUILD/metadata.yaml" \
  --standalone \
  --embed-resources \
  --toc \
  --toc-depth=2 \
  --css="$BUILD/style.css" \
  --include-in-header="$BUILD/header.html" \
  --resource-path="$RESOURCE_PATH" \
  -o "$DIST/bte-book.html"

echo "Building EPUB..."
pandoc "${FILES[@]}" \
  --metadata-file="$BUILD/metadata.yaml" \
  --toc \
  --toc-depth=2 \
  --split-level=1 \
  --epub-title-page=false \
  --epub-cover-image="$BUILD/cover.png" \
  --resource-path="$RESOURCE_PATH" \
  -o "$DIST/bte-book.epub"

echo "Building PDF..."
pandoc "${FILES[@]}" \
  --metadata-file="$BUILD/metadata.yaml" \
  --toc \
  --toc-depth=1 \
  --css="$BUILD/style.css" \
  --pdf-engine=weasyprint \
  --resource-path="$RESOURCE_PATH" \
  -o "$DIST/bte-book.pdf"

echo "Done:"
ls -lh "$DIST"