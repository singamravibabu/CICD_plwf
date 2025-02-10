# This script generates a report file
with open("report.txt", "w") as file:
  file.write("GitHub Actions Artifact Example\n")
  file.write("Report generated successfully!\n")
  file.write("Timestamp: 2025-02-10\n")
print("Report has been generated as 'report.txt'")
