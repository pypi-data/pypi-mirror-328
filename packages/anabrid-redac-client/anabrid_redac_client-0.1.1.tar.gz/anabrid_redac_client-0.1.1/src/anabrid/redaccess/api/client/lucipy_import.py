from typing import List
from lucipy import Circuit


class LucipyImport:
    """
    Lets users import circuits from LUCIPY. Since each circuit created in Lucipy
    is targeted at one cluster, this class lets one build a multi-cluster job
    from multiple LUCIPY circuits.

    Note that this class does _not_ support settings connections between clusters,
    it will just treat every cluster as its own unit.

    Users need to query partition information (number of partitions and size of
    each partition) manually.

    Documentation on how to build lucipy is here:
    https://anabrid.dev/docs/lucipy/dirhtml/compilation/.
    """

    def __init__(
        self, stacks: int = 1, carriers_per_stack: int = 6, with_tx: bool = True
    ):

        self.stacks = stacks
        self.carriers_per_stack = carriers_per_stack

        # create overall initial (empty) document structure
        self.json = {}
        for stack_ix in range(stacks):
            for carrier_ix in range(carriers_per_stack):
                self.json["/" + self.mac(stack_ix, carrier_ix)] = {
                    "/0": self.empty_cluster(),
                    "/1": self.empty_cluster(),
                    "/2": self.empty_cluster(),
                    "/T": {"muxes": 96 * [None]},
                    "adc_channels": [],
                }

                if with_tx and carrier_ix == 0:
                    self.json["/" + self.mac(stack_ix, carrier_ix)]["/ST0"] = {
                        "muxes": 96 * [None]
                    }
                    self.json["/" + self.mac(stack_ix, carrier_ix)]["/ST1"] = {
                        "muxes": 96 * [None]
                    }

    def mac(self, stack: int, carrier: int):
        wing = carrier // 3
        lcl_carrier = carrier % 3

        return f"{stack:02d}-00-{wing:02d}-00-00-{lcl_carrier:02d}"

    def empty_cluster(self):
        return Circuit().generate()

    def import_cluster(
        self,
        circuit: Circuit,
        stack_id: int,
        carrier_id: int,
        cluster_id: int,
        adc_channels: List[int],
    ):
        """
        Import a LUCIDAC circuit, which corresponds to one cluster in the (m)REDAC,
        into one cluster of a carrier inside the current partition. The
        adc_channels specify which of this cluster's ADCs are routed to the
        carrier's ADC channels. Note that when multiple clusters are imported,
        if they set the same ADC channels, the last one becomes effective.

        Args:
            circuit (Circuit): Circuit model from lucipy.
            carrier_id (int): Logical carrier index inside a partition.
            cluster_id (int): Logical cluster index inside the carrier.
            adc_channels (List[int]): A list of ADC channels from the cluster that should be routed to the ADC channels of the carrier, i.e. entering [2,3] here means that channels 2,3 of the cluster will be forwarded to ADCs 2,3 of the carrier.
        """

        # generate config.json by lucipy
        self.json[self.mac(stack_id, carrier_id)][f"/{cluster_id}"] = circuit.generate()

        # add adc channels to carrier
        self.json[self.mac(stack_id, carrier_id)]["adc_channels"] += [
            (16 * cluster_id + l) for l in adc_channels
        ]

    def generate(self):
        return self.json
