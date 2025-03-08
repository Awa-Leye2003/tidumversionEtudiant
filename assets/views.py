from rest_framework import viewsets
from .models import Asset,ScanResult, Port, Application, WebMetadata
from .serializers import AssetSerializer,ScanResultSerializer,PortSerializer, ApplicationSerializer, WebMetadataSerializer
from rest_framework.permissions import AllowAny 
import pandas as pd
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [AllowAny] 

    
class AddAssetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Asset ajouté avec succès", "asset": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateAssetView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            asset = Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            return Response({"error": "Asset introuvable"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AssetSerializer(asset, data=request.data, partial=True)  # `partial=True` permet la mise à jour partielle
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Asset mis à jour avec succès", "asset": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAssetView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            asset = Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            return Response({"error": "Asset introuvable"}, status=status.HTTP_404_NOT_FOUND)

        asset.delete()
        return Response({"message": "Asset supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)


class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer
    permission_classes = [AllowAny]  # Permet à n'importe qui d'envoyer des scans


class PortViewSet(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    permission_classes = [AllowAny]

# Vue pour ajouter un port
class AddPortView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Port ajouté avec succès", "port": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vue pour mettre à jour un port
class UpdatePortView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            port = Port.objects.get(pk=pk)
        except Port.DoesNotExist:
            return Response({"error": "Port introuvable"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PortSerializer(port, data=request.data, partial=True)  # `partial=True` permet la mise à jour partielle
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Port mis à jour avec succès", "port": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vue pour supprimer un port
class DeletePortView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            port = Port.objects.get(pk=pk)
        except Port.DoesNotExist:
            return Response({"error": "Port introuvable"}, status=status.HTTP_404_NOT_FOUND)

        port.delete()
        return Response({"message": "Port supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]

# Vue pour ajouter une application
class AddApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Application ajoutée avec succès", "application": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vue pour mettre à jour une application
class UpdateApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            application = Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            return Response({"error": "Application introuvable"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ApplicationSerializer(application, data=request.data, partial=True)  # `partial=True` permet la mise à jour partielle
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Application mise à jour avec succès", "application": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vue pour supprimer une application
class DeleteApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            application = Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            return Response({"error": "Application introuvable"}, status=status.HTTP_404_NOT_FOUND)

        application.delete()
        return Response({"message": "Application supprimée avec succès"}, status=status.HTTP_204_NO_CONTENT)

# ViewSet pour gérer tous les WebMetadata
class WebMetadataViewSet(viewsets.ModelViewSet):
    queryset = WebMetadata.objects.all()
    serializer_class = WebMetadataSerializer
    permission_classes = [AllowAny] 

# Vue pour ajouter un WebMetadata
class AddWebMetadataView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WebMetadataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "WebMetadata ajouté avec succès", "web_metadata": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vue pour mettre à jour un WebMetadata
class UpdateWebMetadataView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            web_metadata = WebMetadata.objects.get(pk=pk)
        except WebMetadata.DoesNotExist:
            return Response({"error": "WebMetadata introuvable"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WebMetadataSerializer(web_metadata, data=request.data, partial=True)  # `partial=True` permet la mise à jour partielle
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "WebMetadata mis à jour avec succès", "web_metadata": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Vue pour supprimer un WebMetadata
class DeleteWebMetadataView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            web_metadata = WebMetadata.objects.get(pk=pk)
        except WebMetadata.DoesNotExist:
            return Response({"error": "WebMetadata introuvable"}, status=status.HTTP_404_NOT_FOUND)

        web_metadata.delete()
        return Response({"message": "WebMetadata supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({
            "assets": reverse("asset-list", request=request, format=format),
            "assets_add": request.build_absolute_uri(reverse("add-asset")),
            "assets_update": request.build_absolute_uri(reverse("update-asset", args=[1])),  # Exemple avec ID=1
            "assets_delete": request.build_absolute_uri(reverse("delete-asset", args=[1])),  # Exemple avec ID=1
            "scan-results": reverse("scanresult-list", request=request, format=format),
            "ports": reverse("port-list", request=request, format=format),
            "ports_add": request.build_absolute_uri(reverse("add-port")),
            "ports_update": request.build_absolute_uri(reverse("update-port", args=[1])),  # Exemple avec ID=1
            "ports_delete": request.build_absolute_uri(reverse("delete-port", args=[1])),  # Exemple avec ID=1
            "applications": reverse("application-list", request=request, format=format),
            "applications_add": request.build_absolute_uri(reverse("add-application")),
            "applications_update": request.build_absolute_uri(reverse("update-application", args=[1])),  # Exemple avec ID=1
            "applications_delete": request.build_absolute_uri(reverse("delete-application", args=[1])),  # Exemple avec ID=1

            "web-metadata": reverse("webmetadata-list", request=request, format=format),
            "web-metadata_add": request.build_absolute_uri(reverse("add-web-metadata")),
            "web-metadata_update": request.build_absolute_uri(reverse("update-web-metadata", args=[1])),  # Exemple avec ID=1
            "web-metadata_delete": request.build_absolute_uri(reverse("delete-web-metadata", args=[1])),  # Exemple avec ID=1

            "import": request.build_absolute_uri(reverse("import-scan-results")),  # ✅ Vérifie cette ligne !
        })


class ImportScanResultsView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]  # 
    def post(self, request, *args, **kwargs): 
        file = request.FILES.get('file')  
        if not file:
            return Response({"error": "Aucun fichier envoyé"}, status=400)

        try:
            df = pd.read_excel(file)  # 📊 Lire le fichier Excel
        except Exception as e:
            return Response({"error": f"Erreur de lecture du fichier : {str(e)}"}, status=400)

        required_columns = {"asset_id", "scan_date", "port", "protocol", "application", "version"}
        if not required_columns.issubset(df.columns):
            return Response({"error": "Colonnes manquantes. Assurez-vous que le fichier contient : 'asset_id', 'scan_date', 'port', 'protocol', 'application', 'version'."}, status=400)

        for _, row in df.iterrows():
            try:
                asset = Asset.objects.get(id=row["asset_id"])  # 🔎 Vérifie si l'asset existe
                ScanResult.objects.create(
                    asset=asset,
                    scan_date=row["scan_date"],
                    port=row["port"],
                    protocol=row["protocol"],
                    application=row["application"],
                    version=row["version"]
                )
            except Asset.DoesNotExist:
                return Response({"error": f"L'asset avec ID {row['asset_id']} n'existe pas"}, status=400)

        return Response({"message": "Importation réussie"}, status=201)

