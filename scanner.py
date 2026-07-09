from modules.crawler import get_links

print(
    "Python Web Scanner"
)

target = input(
    "\nTarget URL: "
)

links = get_links(
    target
)

print(
    "\nDiscovered Links:"
)

for link in links:

    print(link)
print(
    f"\nTotal Links: {len(links)}"
)