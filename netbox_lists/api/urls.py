from django.urls import path
from rest_framework import routers

from .views import (
    AggregateListViewSet,
    DevicesListViewSet,
    DevicesVMsListView,
    IPAddressListViewSet,
    IPRangeListViewSet,
    ListsRootView,
    PrefixListViewSet,
    PrometheusDeviceSD,
    PrometheusVirtualMachineSD,
    ServiceListviewSet,
    TagsListViewSet,
    VirtualMachinesListViewSet,
)

router = routers.DefaultRouter()
router.APIRootView = ListsRootView

router.register("prefixes", PrefixListViewSet)
router.register("ip-addresses", IPAddressListViewSet)
router.register("ip-ranges", IPRangeListViewSet)
router.register("aggregates", AggregateListViewSet)
router.register("services", ServiceListviewSet)
router.register("tags", TagsListViewSet)
router.register("devices", DevicesListViewSet, basename="devices")
router.register(
    "virtual-machines", VirtualMachinesListViewSet, basename="virtual-machines"
)
router.register("prometheus-devices", PrometheusDeviceSD)
router.register("prometheus-vms", PrometheusVirtualMachineSD)

urlpatterns = [path("devices-vms/", DevicesVMsListView.as_view())]
urlpatterns += router.urls
