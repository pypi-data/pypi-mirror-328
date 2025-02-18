from dataclasses import dataclass
from typing import Union

import qbase58 as base58

from soltxs.normalizer.models import Instruction, Transaction
from soltxs.parser.models import ParsedInstruction, Program
from soltxs.parser.parsers.tokenProgram import TokenProgramParser

WSOL_MINT = "So11111111111111111111111111111111111111112"
SOL_DECIMALS = 9


@dataclass(slots=True)
class Swap(ParsedInstruction):
    """
    Parsed instruction for a Raydium AMM swap.

    Attributes:
        who: The user performing the swap.
        from_token: The token being swapped from.
        from_token_amount: Raw amount of the from token.
        from_token_decimals: Decimals for the from token.
        to_token: The token being swapped to.
        to_token_amount: Raw amount of the to token.
        to_token_decimals: Decimals for the to token.
        minimum_amount_out: Minimum amount expected from the swap.
    """

    who: str
    from_token: str
    from_token_amount: int
    from_token_decimals: int
    to_token: str
    to_token_amount: int
    to_token_decimals: int
    minimum_amount_out: int


ParsedInstructions = Union[Swap]


class _RaydiumAMMParser(Program[ParsedInstructions]):
    """
    Parser for Raydium AMM v4 token swap instructions.
    """

    def __init__(self):
        self.program_id = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
        self.program_name = "RaydiumAMM"
        # Use the first byte of the decoded data as the discriminator.
        self.desc = lambda d: d[0]
        self.desc_map = {9: self.process_Swap}

    def process_Swap(
        self,
        tx: Transaction,
        instruction_index: int,
        decoded_data: bytes,
    ) -> Swap:
        """
        Processes a Swap instruction.

        Args:
            tx: The Transaction object.
            instruction_index: The index of the instruction.
            decoded_data: Decoded instruction data (re-decoded from instruction data).

        Returns:
            A Swap parsed instruction.
        """
        # Retrieve the original instruction.
        instr: Instruction = tx.message.instructions[instruction_index]
        accounts = instr.accounts

        # Re-decode the instruction data (to ensure consistency) using base58.
        decoded_data = base58.decode(instr.data or "")
        # Extract the input amount and minimum output amount.
        amount_in = int.from_bytes(decoded_data[1:9], byteorder="little", signed=False)
        minimum_amount_out = int.from_bytes(decoded_data[9:17], byteorder="little", signed=False)

        # Identify the user accounts based on positions.
        user_source = tx.all_accounts[accounts[-3]]
        user_destination = tx.all_accounts[accounts[-2]]
        who = tx.all_accounts[accounts[-1]]

        # Default token info (assumed to be SOL/WSOL).
        from_token = WSOL_MINT
        from_token_decimals = SOL_DECIMALS
        to_token = WSOL_MINT
        to_token_decimals = SOL_DECIMALS

        # Consolidate token balances from pre and post balances.
        combined_tb = []
        combined_tb.extend(tx.meta.preTokenBalances)
        combined_tb.extend(tx.meta.postTokenBalances)

        for tb in combined_tb:
            token_account = tx.all_accounts[tb.accountIndex]
            if token_account == user_source:
                from_token = tb.mint
                from_token_decimals = tb.uiTokenAmount.decimals
            elif token_account == user_destination:
                to_token = tb.mint
                to_token_decimals = tb.uiTokenAmount.decimals

        to_token_amount = 0
        inner_instrs = []
        # Find inner instructions corresponding to this instruction index.
        for i_group in tx.meta.innerInstructions:
            if i_group.get("index") == instruction_index:
                inner_instrs.extend(i_group["instructions"])
                break

        # Process inner instructions for token transfers.
        for in_instr in inner_instrs:
            prog_id = tx.all_accounts[in_instr["programIdIndex"]]
            if prog_id == TokenProgramParser.program_id:
                action = TokenProgramParser.route_instruction(tx, in_instr)
                if action.instruction_name in ["Transfer", "TransferChecked"] and action.to == user_destination:
                    to_token_amount = action.amount

        return Swap(
            program_id=self.program_id,
            program_name=self.program_name,
            instruction_name="Swap",
            who=who,
            from_token=from_token,
            from_token_amount=amount_in,
            from_token_decimals=from_token_decimals,
            to_token=to_token,
            to_token_amount=to_token_amount,
            to_token_decimals=to_token_decimals,
            minimum_amount_out=minimum_amount_out,
        )


RaydiumAMMParser = _RaydiumAMMParser()
