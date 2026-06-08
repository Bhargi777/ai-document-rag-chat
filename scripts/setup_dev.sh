#!/usr/bin/env bash
set -euo pipefail

echo "Installing frontend dependencies..."
cd "$(dirname "$0")/.."
npm install

echo "Frontend packages installed."
