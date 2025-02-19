import os
import time

from dotenv import load_dotenv
from attps.verify.agent import AgentSDK
from attps.verify.entities import (
    AgentSettings,
    AgentHeader,
    MessageType,
    Priority, AgentMessagePayload, Proofs, AgentMetadata
)
from utils.utils import (
    generate_uuid_v4,
    is_valid_uuid_v4,
    is_valid_address,
    pre_processing_address
)

AGENT_PROXY_ADDRESS = "0x07771A3026E60776deC8C1C61106FB9623521394"
NETWORK_RPC = "https://testnet-rpc.bitlayer.org"

AGENT_PROXY_TYPE_VERSION = "AI Agent Proxy 1.0.0"
AGENT_SETTINGS = AgentSettings(
    signers = [
        "0x4b1056f504f32c678227b5Ae812936249c40AfBF",
        "0xB973476e0cF88a3693014b99f230CEB5A01ac686",
        "0x6cF0803D049a4e8DC01da726A5a212BCB9FAC1a1",
        "0x9D46daa26342e9E9e586A6AdCEDaD667f985567B",
        "0x33AF673aBcE193E20Ee94D6fBEb30fEf0cA7015b",
        "0x868D2dE4a0378450BC62A7596463b30Dc4e3897E",
        "0xD4E157c36E7299bB40800e4aE7909DDcA8097f67",
        "0xA3866A07ABEf3fD0643BD7e1c32600520F465ca8",
        "0x62f642Ae0Ed7F12Bc40F2a9Bf82ccD0a3F3b7531"
    ],
    threshold = 2,
    converter_address="0xaB303EF87774D9D259d1098E9aA4dD6c07F69240",
    agent_header = AgentHeader(
        version =  "1.0",
        message_id="d4d0813f-ceb7-4ce1-8988-12899b26c4b6",
        source_agent_id = "da70f6b3-e580-470f-b88b-caa5369e7778",
        source_agent_name = "APRO Pull Mode Agent",
        target_agent_id = "",
        timestamp =  int(time.time()),
        message_type = MessageType.Event,
        priority = Priority.Low,
        ttl = 60 * 60
    )
)

AGENT_CONTRACT = "0xA1903361Ee8Ec35acC7c8951b4008dbE8D12C155"
AGENT_SETTING_DIGEST = "0x010038164dba6abffb84eb5cb538850d9bc5d8f815149a371069b3255fd177a4"
AGENT_PAYLOAD = AgentMessagePayload(
    data = "0x0006e706cf7ab41fa599311eb3de68be869198ce62aef1cd079475ca50e5b3f60000000000000000000000000000000000000000000000000000000002b1bf0e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000022000000000000000000000000000000000000000000000000000000000000002a0000101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001200003665949c883f9e0f6f002eac32e00bd59dfe6c34e92a91c37d6a8322d6489000000000000000000000000000000000000000000000000000000006762677d000000000000000000000000000000000000000000000000000000006762677d000000000000000000000000000000000000000000000000000003128629ec0800000000000000000000000000000000000000000000000004db732547630000000000000000000000000000000000000000000000000000000000006763b8fd0000000000000000000000000000000000000000000015f0f60671beb95cc0000000000000000000000000000000000000000000000015f083baa654a7b900000000000000000000000000000000000000000000000015f103ec7cb057ea80000000000000000000000000000000000000000000000000000000000000000003b64f7e72208147bb898e8b215d0997967bef0219263726c76995d8a19107d6ba5306a176474f9ccdb1bc5841f97e0592013e404e15b0de0839b81d0efb26179f222e0191269a8560ebd9096707d225bc606d61466b85d8568d7620a3b59a73e800000000000000000000000000000000000000000000000000000000000000037cae0f05c1bf8353eb5db27635f02b40a534d4192099de445764891198231c597a303cd15f302dafbb1263eb6e8e19cbacea985c66c6fed3231fd84a84ebe0276f69f481fe7808c339a04ceb905bb49980846c8ceb89a27b1c09713cb356f773",
    data_hash = "0x53d9f133f1265bd4391fcdf89b63424cbcfd316c8448f76cc515647267ac0a8e",
    proofs = Proofs (
        zk_proof = "0x",
        merkle_proof = "0x",
        signature_proof = "0x000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000001600000000000000000000000000000000000000000000000000000000000000003b64f7e72208147bb898e8b215d0997967bef0219263726c76995d8a19107d6ba5306a176474f9ccdb1bc5841f97e0592013e404e15b0de0839b81d0efb26179f222e0191269a8560ebd9096707d225bc606d61466b85d8568d7620a3b59a73e800000000000000000000000000000000000000000000000000000000000000037cae0f05c1bf8353eb5db27635f02b40a534d4192099de445764891198231c597a303cd15f302dafbb1263eb6e8e19cbacea985c66c6fed3231fd84a84ebe0276f69f481fe7808c339a04ceb905bb49980846c8ceb89a27b1c09713cb356f7730000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001",
    ),
    meta_data = AgentMetadata (
        content_type = "0x",
        encoding= "0x",
        compression= "0x"
    )
)
class TestAgentSDK:
    def setup_method(self):
        load_dotenv()
        user_private_key = os.getenv("USER_PRIVATE_KEY")
        manager_private_key = os.getenv("MANAGER_PRIVATE_KEY")

        self.agent = AgentSDK(endpoint_uri=NETWORK_RPC, proxy_address=AGENT_PROXY_ADDRESS)
        self.user_owner = self.agent.add_account(user_private_key)
        self.manager_owner = self.agent.add_account(manager_private_key)

        print("accounts:", self.agent.accounts())

    def test_type_and_version(self):
        type_version = self.agent.proxy_type_and_version()
        print("type version:", type_version)

        assert type_version == AGENT_PROXY_TYPE_VERSION

    def test_verity(self):
        result = self.agent.verify(
            transmitter= self.user_owner,
            nonce= None,
            agent_contract= AGENT_CONTRACT,
            settings_digest = AGENT_SETTING_DIGEST,
            payload= AGENT_PAYLOAD
        )
        print("verify:", result)

    def test_create_agent(self):
        dynamic_setting = AGENT_SETTINGS
        dynamic_setting.agent_header.source_agent_id = generate_uuid_v4()
        dynamic_setting.agent_header.target_agent_id = generate_uuid_v4()
        dynamic_setting.agent_header.message_id = generate_uuid_v4()
        result = self.agent.create_and_register_agent(
            transmitter = self.user_owner,
            nonce = None,
            settings = AGENT_SETTINGS)
        print("created agent:", result)

    def test_uuid_v4(self):
        uuid = "123e4567-e89b-12d3-a456-426614174000"
        assert is_valid_uuid_v4(uuid) == False

    def test_address(self):
        address = "53d634287d466fa9d6b4c60c822a6c2d261b4c33"
        address = pre_processing_address(address)
        assert is_valid_address(address) == True