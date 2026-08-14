from typing import Dict, List, Optional
from models.block import Block

class Blockchain:
    def __init__(self):
        #Store each block by the unique block_id
        self.blocks : Dict[str, Block] = {}

        #First Block called genesis
        genesis = Block (
            block_id = "genesis",
            parent_id = "",
            miner_type = "genesis",
            height = 0,
            is_main_chain = True
        )
        self.blocks["genesis"] = genesis


        # Current chain heads
        self.public_head_id : str = "genesis"
        self.private_head_id : str = "genesis"

        self.block_counter : int = 0

    @property
    def public_height(self)->int:
          """Current length of the public chain."""
          return self.blocks[self.public_head_id].height
    @property
    def private_height(self)->int:
        """Current length of the private chain."""
        return self.blocks[self.private_head_id].height

    @property
    def private_lead(self)->int: 
        """Lead of private branch over public chain: l_p - l_h."""
        return self.private_height - self.public_height

    def add_block(self, miner_type: str, delay_tau: float = 0.0, is_private: bool = False)->Block:
        """"Creates a block and appends either the public or the private chain"""
        self.block_counter += 1
        new_id = f"block_{self.block_counter}"

        # Determine parent pointer based on whether the block is mined privately
        if is_private:
            parent_id = self.private_head_id
        else:
            parent_id = self.public_head_id
            
        parent_height =self.blocks[parent_id].height

        new_block = Block(
            block_id = new_id,
            parent_id = parent_id,
            miner_type = miner_type,
            height = parent_height + 1,
            delay_tau = delay_tau
        )

        self.blocks[new_id] = new_block

        #Update pointers 
        if is_private:
            self.private_head_id = new_id
        else:
            self.public_head_id = new_id

        return new_block

    def resolve_fork(self, receiver_action : str)-> None:

        """
        Resolves active forks based on Receiver action ('Follow' vs 'Ignore').
        If Receiver chooses 'Follow' on a released private branch, 
        the private head becomes the main public head.
        """
        if receiver_action == "Follow" and self.private_height >= self.public_height:
            # Community switches to private branch
            self.public_head_id = self.private_head_id
        else:
            # Community ignores private branch
             if self.public_height >= self.private_height:
                self.private_head_id = self.public_head_id


    def get_main_chain(self)->List[Block]:
        """
        Backtracks from current public_head to Genesis to return
        the canonical main chain blocks.
        """
        main_chain = []
        curr_id = self.public_head_id

        while curr_id in self.blocks and curr_id != "":
            block = self.blocks[curr_id]
            block.is_main_chain = True
            main_chain.append(block)
            curr_id = block.parent_id

        main_chain.reverse()
        return main_chain

    def calculate_relative_revenue(self)->dict:
        """
        Computes fraction of main chain blocks produced by Selfish vs Honest miners.
        """
        main_chain = self.get_main_chain()
        total_blocks = len(main_chain) - 1 #excludes genesis block

        if total_blocks == 0:
            return{'selfish_share': 0.0, 'honest_share': 0.0}

        selfish_count = sum(1 for b in main_chain if b.miner_type == 'theta_S')
        honest_count = sum(1 for b in main_chain if b.miner_type == 'theta_H')

        return {
            'selfish_share': selfish_count / total_blocks,
            'honest_share': honest_count / total_blocks,
            'total_main_blocks': total_blocks
        }
        





