class Member:
    def __init__(self, name, membership_no):
        self.name = name
        self.membership_no = membership_no

    def __str__(self):
        return f"{self.name} - Membership No: {self.membership_no}"

    def __repr__(self):
        return f"Member('{self.name}', '{self.membership_no}')"
