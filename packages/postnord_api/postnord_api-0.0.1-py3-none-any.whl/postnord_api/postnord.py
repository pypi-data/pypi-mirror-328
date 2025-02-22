from dataclasses import dataclass
import httpx


BASE_URL = "https://api2.postnord.com"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "sv-SE,sv;q=0.8,en-US;q=0.5,en;q=0.3",
    "x-bap-key": "web-tracking-sc",
    "Priority": "u=0",
}


@dataclass
class PostnordAPI:
    shipment_id: str

    def get(self):
        response = httpx.get(
            f"{BASE_URL}/rest/shipment/v1/trackingweb/shipmentInformation",
            headers=headers,
            params={
                "shipmentId": self.shipment_id,
                "locale": "sv",
                "timeZone": "Europe/Stockholm",
            },
        )
        return response.json()
