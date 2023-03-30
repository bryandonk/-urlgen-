# Read in the URLs from a file
with open('urls.txt', 'r') as f:
    urls = f.readlines()

# Read in the replacements from a separate file
replacements_file = 'replacements.txt'
replacements = {}
with open(replacements_file, 'r') as f:
    for line in f:
        key, values = line.strip().split(':')
        replacements[key] = values.split(';')

# Loop through each URL and replace the subfolders
new_urls = []
for url in urls:
    # Split the URL into its component parts
    parts = url.split('/')

    # Loop through each part of the URL and check if it matches a key in the replacements dictionary
    for i, part in enumerate(parts):
        if part in replacements.keys():
            # If the part matches a key, replace it with the corresponding value from the replacements list
            replacement_values = replacements[part]
            if len(replacement_values) > 0:
                # If there are replacement values available, replace the part with the first value in the list
                parts[i] = replacement_values.pop(0)

    # Re-join the modified parts into a new URL
    new_url = '/'.join(parts)
    new_urls.append(new_url)

# Write the modified URLs to a new file
with open('new_urls.txt', 'w') as f:
    for url in new_urls:
        f.write(url)
print(new_urls)