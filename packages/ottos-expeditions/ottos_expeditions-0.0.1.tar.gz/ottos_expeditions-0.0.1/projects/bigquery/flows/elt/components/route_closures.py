import ibis
import ottos_expeditions.lib.transform as T

from ascend.resources import ref, transform


@transform(inputs=[ref("read_router_closures")])
def route_closures(read_router_closures: ibis.Table, context) -> ibis.Table:
    route_closers = T.clean(read_router_closures)

    return route_closers
