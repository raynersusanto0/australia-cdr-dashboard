class DataHolderBrandSummaryModel:
    dataHolderBrandId: str
    interimId: str
    brandName: str
    brandGroup: str
    publicBaseUri: str
    productBaseUri: str
    industries: list[str]
    lastUpdated: str
    abn: str
    acn: str
    arbn: setattr

    def __init__(self, json_data: dict):
        self.dataHolderBrandId = json_data.get("dataHolderBrandId")
        self.interimId = json_data.get("interimId")
        self.brandName = json_data.get("brandName")
        self.brandGroup = json_data.get("brandGroup")
        self.publicBaseUri = json_data.get("publicBaseUri")
        self.productBaseUri = json_data.get("productBaseUri")
        self.industries = json_data.get("industries")
        self.lastUpdated = json_data.get("lastUpdated")
        self.abn = json_data.get("abn")
        self.acn = json_data.get("acn")
        self.arbn = json_data.get("arbn")

    def to_dict(self):
        return {
            "dataHolderBrandId": self.dataHolderBrandId,
            "interimId": self.interimId,
            "brandName": self.brandName,
            "brandGroup": self.brandGroup,
            "publicBaseUri": self.publicBaseUri,
            "productBaseUri": self.productBaseUri,
            "industries": self.industries,
            "lastUpdated": self.lastUpdated,
            "abn": self.abn,
            "acn": self.acn,
            "arbn": self.arbn
        }
    
    def __str__(self) -> str:
        return str(self.to_dict())

    def __repr__(self) -> str:
        return repr(self.to_dict())
