import requests
from DataHolderBrandSummaryModel import DataHolderBrandSummaryModel

def get_banking_brands_summary(base_url: str) -> list[DataHolderBrandSummaryModel]:
    """
    Get banking brands summary from the given base URL.

    Args:
        base_url (str): The base URL to fetch banking brands summary registered in cdr.

    Returns:
        list[DataHolderBrandSummaryModel]: A list of banking brands summary.
    """
    # Placeholder for actual implementation
    uri = f"{base_url}/cdr-register/v1/banking/data-holders/brands/summary"  # Replace with the actual endpoint for banking products

    headers = {
        "Accept": "application/json",
        "x-v": "2"
    }

    response = requests.get(uri, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    brands = response.json().get("data", {})

    return [DataHolderBrandSummaryModel(brand) for brand in brands]

def get_banking_products(product: list[DataHolderBrandSummaryModel]) -> list:
    """
    Get banking products from the given base URL.

    Args:
        base_url (str): The base URL to fetch banking products registered in cdr.

    Returns:
        list: A list of banking products.
    """
    # Placeholder for actual implementation
    versions = ["5", "4", "3", "2", "1"]  # List of versions to try (this showcases some inconsistency in the API versions)
    last_response = None  # Variable to store the last response for error handling
    
    headers = {
        "Accept": "application/json",
    }

    products = list()
    
    for brand in product:
        base_url = brand.productBaseUri

        if not base_url:
            print(f"Brand {brand.brandName} does not have a productBaseUri; skipping...")
            continue  # Skip to the next brand if productBaseUri is missing

        if base_url.endswith("/"):
            base_url = base_url.rstrip("/")  # Remove trailing slash if present

        uri = f"{base_url}/cds-au/v1/banking/products"
        
        for version in versions:
            headers["x-v"] = version
            
            try:
                last_response = requests.get(uri, headers=headers)
            except requests.exceptions.RequestException as error:
                # Some of them don't even work for connection
                print(f"Error fetching products for brand {brand.dataHolderBrandId}: {error}")
                break

            if last_response.status_code == 406:
                print(f"{uri} does not support x-v {version}; trying next version")
                continue

            if last_response.status_code != 200:
                print(f"{uri} returned {last_response.status_code}; skipping...")
                break  # Skip to the next brand if access is forbidden

            if last_response.status_code == 200:
                print(f"Successfully fetched products for brand {brand.brandName} with x-v {version}")
                products.extend(last_response.json().get("data", {}))
                break  # Exit the version loop if successful

            last_response.raise_for_status()
        
        assert last_response is not None, f"All versions failed for {uri}"

    return products

def main():
    base_url = "https://api.cdr.gov.au"  # Replace with the actual base URL
    brands = get_banking_brands_summary(base_url)
    products = get_banking_products(brands)
    print(f"Total banking products fetched: {len(products)}")
    print(products)
     # Print the dataHolderBrandId of the first product

if __name__ == "__main__":
    main()
