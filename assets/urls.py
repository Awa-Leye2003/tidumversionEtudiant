from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, ScanResultViewSet, AddApplicationView, UpdateApplicationView, DeleteApplicationView,PortViewSet,APIRootView,AddPortView, UpdatePortView, DeletePortView, ImportScanResultsView, ApplicationViewSet, WebMetadataViewSet ,AddAssetView, UpdateAssetView, DeleteAssetView ,AddWebMetadataView, UpdateWebMetadataView, DeleteWebMetadataView

router = DefaultRouter()
router.register(r'assets', AssetViewSet, basename='asset')
router.register(r'scan-results', ScanResultViewSet)
router.register(r'port', PortViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'web-metadata', WebMetadataViewSet)

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('', include(router.urls)),  # Inclure toutes les routes générées
    # Endpoints CRUD personnalisés pour les assets
    path('assets/add/', AddAssetView.as_view(), name='add-asset'),
    path('assets/update/<int:pk>/', UpdateAssetView.as_view(), name='update-asset'),
    path('assets/delete/<int:pk>/', DeleteAssetView.as_view(), name='delete-asset'),

    path('import/', ImportScanResultsView.as_view(), name='import-scan-results'),

    # Endpoints CRUD personnalisés pour les ports
    path('ports/add/', AddPortView.as_view(), name='add-port'),
    path('ports/update/<int:pk>/', UpdatePortView.as_view(), name='update-port'),
    path('ports/delete/<int:pk>/', DeletePortView.as_view(), name='delete-port'),

     # Endpoints CRUD personnalisés pour les applications
    path('applications/add/', AddApplicationView.as_view(), name='add-application'),
    path('applications/update/<int:pk>/', UpdateApplicationView.as_view(), name='update-application'),
    path('applications/delete/<int:pk>/', DeleteApplicationView.as_view(), name='delete-application'),
 

    path('web-metadata/add/', AddWebMetadataView.as_view(), name='add-web-metadata'),
    path('web-metadata/update/<int:pk>/', UpdateWebMetadataView.as_view(), name='update-web-metadata'),
    path('web-metadata/delete/<int:pk>/', DeleteWebMetadataView.as_view(), name='delete-web-metadata'),



   
]





 












