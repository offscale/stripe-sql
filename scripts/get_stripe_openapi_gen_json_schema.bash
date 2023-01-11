#!/usr/bin/env bash

set -euo pipefail

declare -r DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for dep in unzip curl jq sort sed mkdir; do
   if ! command -v "$dep" &>/dev/null; then
     printf 'Missing dependency: %s\n' "$dep" 1>&2
     exit 1
   fi
done

declare -r zipfile="$DIR"'/stripe-openapi.zip'
if [ ! -f "$zipfile" ]; then
  curl -L 'https://api.github.com/repos/stripe/openapi/zipball' -o "$zipfile"
  unzip "$zipfile" -d "$DIR"
fi

declare -r root="$(cd "$(dirname "${DIR}")" && pwd)"'/json_schemas'
mkdir -p "$root"
declare -r json_file="$root"'/customers.json'
declare -r spec_json_file="$(compgen -G "${DIR}/stripe-openapi*/")"'openapi/spec3.sdk.json'
jq '.components.schemas.customer' "$spec_json_file" > "$json_file"
printf 'Wrote %s\n' "$json_file"

while read -r ref; do
  ref_json_file="$root"'/'"${ref##*.}"'.json'
  res="$(jq "$ref" "$spec_json_file")"
  if [ "$res" != 'null' ]; then
    printf '%s' "$res" > "$ref_json_file"
    printf 'Wrote %s\n' "$ref_json_file"
  fi
done < <(jq -r '..|objects|select(has("$ref"))|."$ref"' "$spec_json_file" | sort -u | sed 's|/|.|g; s/^#//;')
