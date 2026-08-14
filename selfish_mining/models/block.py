from dataclasses import dataclass, field
import time


@dataclass
class Block:
    block_id : str
    parent_id : str 
    miner_type : str
    height : int
    timestamp : float = field(default_factory = time.time)
    delay_tau : float = 0.0 #signal value
    is_main_chain : bool = True
    # accepted : bool  = False


