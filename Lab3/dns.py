import dns.resolver

class DNSResolver:
    def init(self):
        self.resolver = dns.resolver.Resolver(configure=False)
        self.resolver.nameservers = ['8.8.8.8']  

    def resolve_domain(self, domain):
        try:
            answers = self.resolver.resolve(domain, 'A')
            ip_addresses = [answer.address for answer in answers]
            return ip_addresses
        except dns.resolver.NXDOMAIN:
            return None

    def resolve_address(self, ip):
        try:
            result = self.resolver.resolve_address(ip)
            return [data.target.to_text() for data in result]
        except dns.resolver.NoAnswer:
            return None

    def set_dns_server(self, dns_ip):
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_ip]
        try:
            resolver.resolve('google.com')
            self.resolver.nameservers = [dns_ip]
            return f"DNS server set to {dns_ip}"
        except (dns.resolver.NoNameservers, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            return f"Invalid DNS server: {dns_ip}"

if name == "main":
    resolver = DNSResolver()
    while True:
        user_input = input("Introduceți comanda: ")
        parts = user_input.split()
        if len(parts) < 2:
            print("Comandă invalidă. Utilizare: resolve <domain> sau resolve <ip>")
            continue

        command, value = parts[0], parts[1]

        if command == "resolve":
            if value.startswith("http://") or value.startswith("https://"):
                value = value.split("//")[1]
            result = resolver.resolve_domain(value)
            if not result:
                ip_result = resolver.resolve_address(value)
                if ip_result:
                    print(f"Domain associated with IP {value}: {ip_result}")
                else:
                    print(f"No domain found for IP {value}")
            else:
                print(result)
        elif command == "use" and value == "dns":
            if len(parts) < 3:
                print("Comandă invalidă. Utilizare: use dns <ip>")
                continue
            dns_ip = parts[2]
            print(resolver.set_dns_server(dns_ip))
        else:
            print("Comandă invalidă. Utilizare: resolve <domain> sau resolve <ip>")
