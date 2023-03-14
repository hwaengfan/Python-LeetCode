class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = set()
        for email in emails:
            localName, domainName = email.split("@")
            localName = localName.split("+")[0]
            localName = localName.replace(".", "")
            uniqueEmail.add(localName + "@" + domainName)
        return len(uniqueEmail)
