#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import vtkActor

from SpatialView.node_data.vtk_mapper_data import VtkMapperData
from .node_model_template import NodeModelTemplate, withModel, withPort
from .vtk_renderer import Renderer


@withModel(
    capStr="Vtk Actor",
    category="Displays",
)
class VtkDisplayActorModel(NodeModelTemplate):
    # ==========================================================================
    # =========== Blinn-Phong ==================================================
    # ==========================================================================

    # =========== Ambient ======================================================
    @property
    def ambientMax(self):
        return self._actor.GetProperty().GetAmbientMaxValue()

    @property
    def ambientMin(self):
        return self._actor.GetProperty().GetAmbientMinValue()

    @property
    def ambient(self):
        return self._actor.GetProperty().GetAmbient()

    @ambient.setter
    def ambient(self, value):
        self._actor.GetProperty().SetAmbient(value)

    @property
    def ambientColor(self):
        return self._actor.GetProperty().GetAmbientColor()

    @ambientColor.setter
    def ambientColor(self, value):
        self._actor.GetProperty().SetAmbientColor(value)

    # =========== Diffuse ======================================================
    @property
    def diffuseMax(self):
        return self._actor.GetProperty().GetDiffuseMaxValue()

    @property
    def diffuseMin(self):
        return self._actor.GetProperty().GetDiffuseMinValue()

    @property
    def diffuse(self):
        return self._actor.GetProperty().GetDiffuse()

    @diffuse.setter
    def diffuse(self, value):
        self._actor.GetProperty().SetDiffuse(value)

    @property
    def diffuseColor(self):
        return self._actor.GetProperty().GetDiffuseColor()

    @diffuseColor.setter
    def diffuseColor(self, value):
        self._actor.GetProperty().SetDiffuseColor(value)

    # =========== Specular ======================================================
    @property
    def specularMax(self):
        return self._actor.GetProperty().GetSpecularMaxValue()

    @property
    def specularMin(self):
        return self._actor.GetProperty().GetSpecularMinValue()

    @property
    def specular(self):
        return self._actor.GetProperty().GetSpecular()

    @specular.setter
    def specular(self, value):
        self._actor.GetProperty().SetSpecular(value)

    @property
    def specularColor(self):
        return self._actor.GetProperty().GetSpecularColor()

    @specularColor.setter
    def specularColor(self, value):
        self._actor.GetProperty().SetSpecularColor(value)

    # =========== Specular Power ======================================================
    @property
    def specularPowerMax(self):
        return self._actor.GetProperty().GetSpecularPowerMaxValue()

    @property
    def specularPowerMin(self):
        return self._actor.GetProperty().GetSpecularPowerMinValue()

    @property
    def specularPower(self):
        return self._actor.GetProperty().GetSpecularPower()

    @specularPower.setter
    def specularPower(self, value):
        self._actor.GetProperty().SetSpecularPower(value)

    # =========== Color ======================================================

    @property
    def color(self):
        return self._actor.GetProperty().GetColor()

    @color.setter
    def color(self, value):
        self._actor.GetProperty().SetColor(value)

    @property
    def baseColorTexture(self):
        return self._actor.GetProperty().GetTexture("baseColor")

    @baseColorTexture.setter
    def baseColorTexture(self, value):
        self._actor.GetProperty().SetBaseColorTexture(value)

    # ============================================================================
    # =========== PBR =============================================================
    # =============================================================================

    # =========== Anisotropy ======================================================
    @property
    def anisotropyMax(self):
        return self._actor.GetProperty().GetAnisotropyMaxValue()

    @property
    def anisotropyMin(self):
        return self._actor.GetProperty().GetAnisotropyMinValue()

    @property
    def anisotropy(self):
        return self._actor.GetProperty().GetAnisotropy()

    @anisotropy.setter
    def anisotropy(self, value):
        self._actor.GetProperty().SetAnisotropy(value)

    @property
    def anisotropyRotationMax(self):
        return self._actor.GetProperty().GetAnisotropyRotationMaxValue()

    @property
    def anisotropyRotationMin(self):
        return self._actor.GetProperty().GetAnisotropyRotationMinValue()

    @property
    def anisotropyRotation(self):
        return self._actor.GetProperty().GetAnisotropyRotation()

    @anisotropyRotation.setter
    def anisotropyRotation(self, value):
        self._actor.GetProperty().SetAnisotropyRotation(value)

    @property
    def anisotropyTexture(self):
        # todo
        return self._actor.GetProperty().GetTexture("anisotropy")

    @anisotropyTexture.setter
    def anisotropyTexture(self, value):
        self._actor.GetProperty().SetAnisotropyTexture(value)

    # =========== IOR ======================================================
    @property
    def baseIORMax(self):
        return self._actor.GetProperty().GetBaseIORMaxValue()

    @property
    def baseIORMin(self):
        return self._actor.GetProperty().GetBaseIORMinValue()

    @property
    def baseIOR(self):
        return self._actor.GetProperty().GetBaseIOR()

    @baseIOR.setter
    def baseIOR(self, value):
        self._actor.GetProperty().SetBaseIOR(value)

    @property
    def coatIORMax(self):
        return self._actor.GetProperty().GetCoatIORMaxValue()

    @property
    def coatIORMin(self):
        return self._actor.GetProperty().GetCoatIORMinValue()

    @property
    def coatIOR(self):
        return self._actor.GetProperty().GetCoatIOR()

    @coatIOR.setter
    def coatIOR(self, value):
        self._actor.GetProperty().SetCoatIOR(value)

    # =========== Coat ======================================================
    @property
    def coatColor(self):
        return self._actor.GetProperty().GetCoatColor()

    @coatColor.setter
    def coatColor(self, value):
        self._actor.GetProperty().SetCoatColor(value)

    @property
    def coatStrengthMax(self):
        return self._actor.GetProperty().GetCoatStrengthMaxValue()

    @property
    def coatStrengthMin(self):
        return self._actor.GetProperty().GetCoatStrengthMinValue()

    @property
    def coatStrength(self):
        return self._actor.GetProperty().GetCoatStrength()

    @coatStrength.setter
    def coatStrength(self, value):
        self._actor.GetProperty().SetCoatStrength(value)

    @property
    def coatNormalTexture(self):
        return self._actor.GetProperty().GetTexture("coatNormal")

    @coatNormalTexture.setter
    def coatNormalTexture(self, value):
        self._actor.GetProperty().SetCoatNormalTexture(value)

    @property
    def coatNormalScaleMax(self):
        return self._actor.GetProperty().GetCoatNormalScaleMaxValue()

    @property
    def coatNormalScaleMin(self):
        return self._actor.GetProperty().GetCoatNormalScaleMinValue()

    @property
    def coatNormalScale(self):
        return self._actor.GetProperty().GetCoatNormalScale()

    @coatNormalScale.setter
    def coatNormalScale(self, value):
        self._actor.GetProperty().SetCoatNormalScale(value)

    @property
    def coatRoughnessMax(self):
        return self._actor.GetProperty().GetCoatRoughnessMaxValue()

    @property
    def coatRoughnessMin(self):
        return self._actor.GetProperty().GetCoatRoughnessMinValue()

    @property
    def coatRoughness(self):
        return self._actor.GetProperty().GetCoatRoughness()

    @coatRoughness.setter
    def coatRoughness(self, value):
        self._actor.GetProperty().SetCoatRoughness(value)

    # =========== Emissive ======================================================
    @property
    def emissiveFactor(self):
        return self._actor.GetProperty().GetEmissiveFactor()

    @emissiveFactor.setter
    def emissiveFactor(self, value):
        self._actor.GetProperty().SetEmissiveFactor(value)

    @property
    def emissiveTexture(self):
        return self._actor.GetProperty().GetTexture("emissiveTexture")

    @emissiveTexture.setter
    def emissiveTexture(self, value):
        self._actor.GetProperty().SetEmissiveTexture(value)

    # =========== Normal ======================================================
    @property
    def normalScale(self):
        return self._actor.GetProperty().GetNormalScale()

    @normalScale.setter
    def normalScale(self, value):
        self._actor.GetProperty().SetNormalScale(value)

    @property
    def normalTexture(self):
        return self._actor.GetProperty().GetTexture("normalTexture")

    @normalTexture.setter
    def normalTexture(self, value):
        self._actor.GetProperty().SetNormalTexture(value)

    # =========== Metallic ======================================================
    @property
    def metallicMax(self):
        return self._actor.GetProperty().GetMetallicMaxValue()

    @property
    def metallicMin(self):
        return self._actor.GetProperty().GetMetallicMinValue()

    @property
    def metallic(self):
        return self._actor.GetProperty().GetMetallic()

    @metallic.setter
    def metallic(self, value):
        self._actor.GetProperty().SetMetallic(value)

    # =========== Roughness ======================================================
    @property
    def roughnessMax(self):
        return self._actor.GetProperty().GetRoughnessMaxValue()

    @property
    def roughnessMin(self):
        return self._actor.GetProperty().GetRoughnessMinValue()

    @property
    def roughness(self):
        return self._actor.GetProperty().GetRoughness()

    @roughness.setter
    def roughness(self, value):
        self._actor.GetProperty().SetRoughness(value)

    # =========== OcclusionStrength ======================================================
    @property
    def occlusionStrengthMax(self):
        return self._actor.GetProperty().GetOcclusionStrengthMaxValue()

    @property
    def occlusionStrengthMin(self):
        return self._actor.GetProperty().GetOcclusionStrengthMinValue()

    @property
    def occlusionStrength(self):
        return self._actor.GetProperty().GetOcclusionStrength()

    @occlusionStrength.setter
    def occlusionStrength(self, value):
        self._actor.GetProperty().SetOcclusionStrength(value)

    # =========== Edge ======================================================
    @property
    def edgeTint(self):
        return self._actor.GetProperty().GetEdgeTint()

    @edgeTint.setter
    def edgeTint(self, value):
        self._actor.GetProperty().SetEdgeTint(value)

    @property
    def edgeColor(self):
        return self._actor.GetProperty().GetEdgeColor()

    @edgeColor.setter
    def edgeColor(self, value):
        self._actor.GetProperty().SetEdgeColor(value)

    @property
    def edgeOpacityMax(self):
        return self._actor.GetProperty().GetEdgeOpacityMaxValue()

    @property
    def edgeOpacityMin(self):
        return self._actor.GetProperty().GetEdgeOpacityMinValue()

    @property
    def edgeOpacity(self):
        return self._actor.GetProperty().GetEdgeOpacity()

    @edgeOpacity.setter
    def edgeOpacity(self, value):
        self._actor.GetProperty().SetEdgeOpacity(value)

    @property
    def edgeVisibility(self):
        return self._actor.GetProperty().GetEdgeVisibility()

    @edgeVisibility.setter
    def edgeVisibility(self, value):
        self._actor.GetProperty().SetEdgeVisible(value)

    # =========== Line ======================================================
    @property
    def lineWidthMax(self):
        return self._actor.GetProperty().GetLineWidthMaxValue()

    @property
    def lineWidthMin(self):
        return self._actor.GetProperty().GetLineWidthMinValue()

    @property
    def lineWidth(self):
        return self._actor.GetProperty().GetLineWidth()

    @lineWidth.setter
    def lineWidth(self, value):
        self._actor.GetProperty().SetLineWidth(value)

    @property
    def lineStippleRepeatFactorMax(self):
        return self._actor.GetProperty().GetLineStippleRepeatFactorMaxValue()

    @property
    def lineStippleRepeatFactorMin(self):
        return self._actor.GetProperty().GetLineStippleRepeatFactorMinValue()

    @property
    def lineStippleRepeatFactor(self):
        return self._actor.GetProperty().GetLineStippleRepeatFactor()

    @lineStippleRepeatFactor.setter
    def lineStippleRepeatFactor(self, value):
        self._actor.GetProperty().SetLineStippleRepeatFactor(value)

    @property
    def lineStipplePattern(self):
        return self._actor.GetProperty().GetLineStipplePattern()

    @lineStipplePattern.setter
    def lineStipplePattern(self, value):
        self._actor.GetProperty().SetLineStipplePattern(value)

    # =========== Vertex ======================================================
    @property
    def vertexColor(self):
        return self._actor.GetProperty().GetVertexColor()

    @vertexColor.setter
    def vertexColor(self, value):
        self._actor.GetProperty().SetVertexColor(value)

    @property
    def vertexVisibility(self):
        return self._actor.GetProperty().GetVertexVisibility()

    @vertexVisibility.setter
    def vertexVisibility(self, value):
        self._actor.GetProperty().SetVertexVisibility(value)

    # =========== Point ======================================================
    @property
    def pointSizeMax(self):
        return self._actor.GetProperty().GetPointSizeMaxValue()

    @property
    def pointSizeMin(self):
        return self._actor.GetProperty().GetPointSizeMinValue()

    @property
    def pointSize(self):
        return self._actor.GetProperty().GetPointSize()

    @pointSize.setter
    def pointSize(self, value):
        self._actor.GetProperty().SetPointSize(value)

    # =========== ORM ======================================================
    @property
    def ORMTexture(self):
        return self._actor.GetProperty().GetTexture("ORMTexture")

    @ORMTexture.setter
    def ORMTexture(self, value):
        self._actor.GetProperty().SetORMTexture(value)

    # =========== Opacity ======================================================
    @property
    def opacityMax(self):
        return self._actor.GetProperty().GetOpacityMaxValue()

    @property
    def opacityMin(self):
        return self._actor.GetProperty().GetOpacityMinValue()

    @property
    def opacity(self):
        return self._actor.GetProperty().GetOpacity()

    @opacity.setter
    def opacity(self, value):
        self._actor.GetProperty().SetOpacity(value)

    # =========== Culling ======================================================
    @property
    def backFaceCulling(self):
        return self._actor.GetProperty().GetBackfaceCulling()

    @backFaceCulling.setter
    def backFaceCulling(self, value):
        self._actor.GetProperty().SetBackfaceCulling(value)

    @property
    def frontFaceCulling(self):
        return self._actor.GetProperty().GetFrontfaceCulling()

    @frontFaceCulling.setter
    def frontFaceCulling(self, value):
        self._actor.GetProperty().SetFrontfaceCulling(value)

    @property
    def showTexturesOnBackface(self):
        return self._actor.GetProperty().GetShowTexturesOnBackface()

    @showTexturesOnBackface.setter
    def showTexturesOnBackface(self, value):
        self._actor.GetProperty().SetShowTexturesOnBackface(value)

    # =========== Interpolation ======================================================
    @property
    def interpolationMax(self):
        return self._actor.GetProperty().GetInterpolationMaxValue()

    @property
    def interpolationMin(self):
        return self._actor.GetProperty().GetInterpolationMinValue()

    @property
    def interpolation(self):
        return self._actor.GetProperty().GetInterpolation()

    def interpolationString(self):
        return self._actor.GetProperty().GetInterpolationAsString()

    @interpolation.setter
    def interpolation(self, value):
        self._actor.GetProperty().SetInterpolation(value)

    # =========== Representation ======================================================
    @property
    def representationMax(self):
        return self._actor.GetProperty().GetRepresentationMaxValue()

    @property
    def representationMin(self):
        return self._actor.GetProperty().GetRepresentationMinValue()

    @property
    def representation(self):
        return self._actor.GetProperty().GetRepresentation()

    def representationString(self):
        return self._actor.GetProperty().GetRepresentationAsString()

    @representation.setter
    def representation(self, value):
        self._actor.GetProperty().SetRepresentation(value)

    # =========== Render Present ======================================================
    @property
    def renderPointsAsSpheres(self):
        return self._actor.GetProperty().GetRenderPointsAsSpheres()

    @renderPointsAsSpheres.setter
    def renderPointsAsSpheres(self, value):
        self._actor.GetProperty().SetRenderPointsAsSpheres(value)

    @property
    def renderLinesAsTubes(self):
        return self._actor.GetProperty().GetRenderLinesAsTubes()

    @renderLinesAsTubes.setter
    def renderLinesAsTubes(self, value):
        self._actor.GetProperty().SetRenderLinesAsTubes(value)

    # =========== Selection ======================================================
    @property
    def selectionColor(self):
        return self._actor.GetProperty().GetSelectionColor()

    @selectionColor.setter
    def selectionColor(self, value):
        self._actor.GetProperty().SetSelectionColor(value)

    @property
    def selectionLineWidth(self):
        return self._actor.GetProperty().GetSelectionLineWidth()

    @selectionLineWidth.setter
    def selectionLineWidth(self, value):
        self._actor.GetProperty().SetSelectionLineWidth(value)

    @property
    def selectionPointSize(self):
        return self._actor.GetProperty().GetSelectionPointSize()

    @selectionPointSize.setter
    def selectionPointSize(self, value):
        self._actor.GetProperty().SetSelectionPointSize(value)

    # =========== Mapper ======================================================
    @property
    def mapper(self):
        return self._actor.GetMapper()

    @mapper.setter
    def mapper(self, value):
        self._actor.SetMapper(value)

    @property
    def inPort(self):
        return self.mapper

    @withPort(0, sNode.PortType.In, VtkMapperData)
    @inPort.setter
    def inPort(self, value):
        self.mapper = value.mapper()

    def __init__(self):
        super().__init__()
        self._actor = vtkActor()
        Renderer().handle.AddActor(self._actor)
