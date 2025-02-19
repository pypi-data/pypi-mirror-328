import json
from typing import List
from unittest.mock import patch

from agentstr.buyer import BuyerTools
from agentstr.models import AgentProfile, MerchantProduct, MerchantStall, NostrProfile
from agentstr.nostr import Keys


def test_buyer_profile_creation(
    buyer_profile: AgentProfile,
    buyer_profile_name: str,
    buyer_profile_about: str,
    buyer_profile_picture: str,
) -> None:
    assert buyer_profile.get_name() == buyer_profile_name
    assert buyer_profile.get_about() == buyer_profile_about
    assert buyer_profile.get_picture() == buyer_profile_picture


def test_find_sellers_by_location(
    buyer_tools: BuyerTools, merchant_location: str, merchant_profile_name: str
) -> None:
    with patch(
        "agentstr.buyer._map_location_to_geohash"
    ) as mock_map_location_to_geohash:
        mock_map_location_to_geohash.return_value = "000000000"

        result = buyer_tools.find_sellers_by_location(merchant_location)
        assert result is not None
        assert merchant_profile_name in result


def test_find_seller_by_name(
    buyer_tools: BuyerTools,
    merchant_profile_name: str,
) -> None:
    result = buyer_tools.find_seller_by_name(merchant_profile_name)
    assert result is not None
    assert merchant_profile_name in result


def test_find_seller_by_public_key(
    buyer_tools: BuyerTools,
    merchant_keys: Keys,
    seller_nostr_profile: NostrProfile,
) -> None:
    with patch.object(
        buyer_tools, "find_seller_by_public_key"
    ) as mock_find_seller_by_public_key:
        mock_find_seller_by_public_key.return_value = seller_nostr_profile.to_json()

        result = buyer_tools.find_seller_by_public_key(
            merchant_keys.public_key().to_bech32()
        )
        assert result is not None
        assert merchant_keys.public_key().to_bech32() in result


def test_get_seller_stalls(
    buyer_tools: BuyerTools,
    seller_nostr_profile: NostrProfile,
    merchant_stalls: List[MerchantStall],
) -> None:
    with patch.object(
        buyer_tools._nostr_client, "retrieve_stalls_from_seller"
    ) as mock_get_seller_stalls:
        mock_get_seller_stalls.return_value = merchant_stalls

        result = buyer_tools.get_seller_stalls(seller_nostr_profile.get_public_key())
        assert result is not None


def test_get_seller_products(
    buyer_tools: BuyerTools,
    merchant_products: List[MerchantProduct],
    seller_nostr_profile: NostrProfile,
) -> None:
    with patch.object(
        buyer_tools._nostr_client,
        "retrieve_products_from_seller",
        return_value=merchant_products,
    ) as mock_get_seller_products:
        result = buyer_tools.get_seller_products(seller_nostr_profile.get_public_key())
        assert isinstance(result, str)  # Ensure it's a JSON string

        products = json.loads(result)  # Convert JSON string back to a Python list
        assert isinstance(products, list)  # Ensure it's a list
        assert len(products) > 0  # Ensure the list is not empty
        assert isinstance(products[0], dict)  # Ensure the first item is a dictionary
        assert "name" in products[0]  # Ensure "name" key exists in the first product
