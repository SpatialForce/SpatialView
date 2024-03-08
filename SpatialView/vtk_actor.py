#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkRenderingCore import vtkActor


class VtkActor:
    def __init__(self):
        self.actor = vtkActor()

    # ==========================================================================
    # =========== Blinn-Phong ==================================================
    # ==========================================================================

    # =========== Ambient ======================================================
    @property
    def ambientMax(self):
        return self.actor.GetProperty().GetAmbientMaxValue()

    @property
    def ambientMin(self):
        return self.actor.GetProperty().GetAmbientMinValue()

    @property
    def ambient(self):
        return self.actor.GetProperty().GetAmbient()

    @ambient.setter
    def ambient(self, value):
        self.actor.GetProperty().SetAmbient(value)

    @property
    def ambientColor(self):
        return self.actor.GetProperty().GetAmbientColor()

    @ambientColor.setter
    def ambientColor(self, value):
        self.actor.GetProperty().SetAmbientColor(value)

    # =========== Diffuse ======================================================
    @property
    def diffuseMax(self):
        return self.actor.GetProperty().GetDiffuseMaxValue()

    @property
    def diffuseMin(self):
        return self.actor.GetProperty().GetDiffuseMinValue()

    @property
    def diffuse(self):
        return self.actor.GetProperty().GetDiffuse()

    @diffuse.setter
    def diffuse(self, value):
        self.actor.GetProperty().SetDiffuse(value)

    @property
    def diffuseColor(self):
        return self.actor.GetProperty().GetDiffuseColor()

    @diffuseColor.setter
    def diffuseColor(self, value):
        self.actor.GetProperty().SetDiffuseColor(value)

    # =========== Specular ======================================================
    @property
    def specularMax(self):
        return self.actor.GetProperty().GetSpecularMaxValue()

    @property
    def specularMin(self):
        return self.actor.GetProperty().GetSpecularMinValue()

    @property
    def specular(self):
        return self.actor.GetProperty().GetSpecular()

    @specular.setter
    def specular(self, value):
        self.actor.GetProperty().SetSpecular(value)

    @property
    def specularColor(self):
        return self.actor.GetProperty().GetSpecularColor()

    @specularColor.setter
    def specularColor(self, value):
        self.actor.GetProperty().SetSpecularColor(value)

    # =========== Specular Power ======================================================
    @property
    def specularPowerMax(self):
        return self.actor.GetProperty().GetSpecularPowerMaxValue()

    @property
    def specularPowerMin(self):
        return self.actor.GetProperty().GetSpecularPowerMinValue()

    @property
    def specularPower(self):
        return self.actor.GetProperty().GetSpecularPower()

    @specularPower.setter
    def specularPower(self, value):
        self.actor.GetProperty().SetSpecularPower(value)

    # =========== Color ======================================================

    @property
    def color(self):
        return self.actor.GetProperty().GetColor()

    @color.setter
    def color(self, value):
        self.actor.GetProperty().SetColor(value)

    @property
    def baseColorTexture(self):
        return self.actor.GetProperty().GetTexture("baseColor")

    @baseColorTexture.setter
    def baseColorTexture(self, value):
        self.actor.GetProperty().SetBaseColorTexture(value)

    # ============================================================================
    # =========== PBR =============================================================
    # =============================================================================

    # =========== Anisotropy ======================================================
    @property
    def anisotropyMax(self):
        return self.actor.GetProperty().GetAnisotropyMaxValue()

    @property
    def anisotropyMin(self):
        return self.actor.GetProperty().GetAnisotropyMinValue()

    @property
    def anisotropy(self):
        return self.actor.GetProperty().GetAnisotropy()

    @anisotropy.setter
    def anisotropy(self, value):
        self.actor.GetProperty().SetAnisotropy(value)

    @property
    def anisotropyRotationMax(self):
        return self.actor.GetProperty().GetAnisotropyRotationMaxValue()

    @property
    def anisotropyRotationMin(self):
        return self.actor.GetProperty().GetAnisotropyRotationMinValue()

    @property
    def anisotropyRotation(self):
        return self.actor.GetProperty().GetAnisotropyRotation()

    @anisotropyRotation.setter
    def anisotropyRotation(self, value):
        self.actor.GetProperty().SetAnisotropyRotation(value)

    @property
    def anisotropyTexture(self):
        # todo
        return self.actor.GetProperty().GetTexture("anisotropy")

    @anisotropyTexture.setter
    def anisotropyTexture(self, value):
        self.actor.GetProperty().SetAnisotropyTexture(value)

    # =========== IOR ======================================================
    @property
    def baseIORMax(self):
        return self.actor.GetProperty().GetBaseIORMaxValue()

    @property
    def baseIORMin(self):
        return self.actor.GetProperty().GetBaseIORMinValue()

    @property
    def baseIOR(self):
        return self.actor.GetProperty().GetBaseIOR()

    @baseIOR.setter
    def baseIOR(self, value):
        self.actor.GetProperty().SetBaseIOR(value)

    @property
    def coatIORMax(self):
        return self.actor.GetProperty().GetCoatIORMaxValue()

    @property
    def coatIORMin(self):
        return self.actor.GetProperty().GetCoatIORMinValue()

    @property
    def coatIOR(self):
        return self.actor.GetProperty().GetCoatIOR()

    @coatIOR.setter
    def coatIOR(self, value):
        self.actor.GetProperty().SetCoatIOR(value)

    # =========== Coat ======================================================
    @property
    def coatColor(self):
        return self.actor.GetProperty().GetCoatColor()

    @coatColor.setter
    def coatColor(self, value):
        self.actor.GetProperty().SetCoatColor(value)

    @property
    def coatStrengthMax(self):
        return self.actor.GetProperty().GetCoatStrengthMaxValue()

    @property
    def coatStrengthMin(self):
        return self.actor.GetProperty().GetCoatStrengthMinValue()

    @property
    def coatStrength(self):
        return self.actor.GetProperty().GetCoatStrength()

    @coatStrength.setter
    def coatStrength(self, value):
        self.actor.GetProperty().SetCoatStrength(value)

    @property
    def coatNormalTexture(self):
        return self.actor.GetProperty().GetTexture("coatNormal")

    @coatNormalTexture.setter
    def coatNormalTexture(self, value):
        self.actor.GetProperty().SetCoatNormalTexture(value)

    @property
    def coatNormalScaleMax(self):
        return self.actor.GetProperty().GetCoatNormalScaleMaxValue()

    @property
    def coatNormalScaleMin(self):
        return self.actor.GetProperty().GetCoatNormalScaleMinValue()

    @property
    def coatNormalScale(self):
        return self.actor.GetProperty().GetCoatNormalScale()

    @coatNormalScale.setter
    def coatNormalScale(self, value):
        self.actor.GetProperty().SetCoatNormalScale(value)

    @property
    def coatRoughnessMax(self):
        return self.actor.GetProperty().GetCoatRoughnessMaxValue()

    @property
    def coatRoughnessMin(self):
        return self.actor.GetProperty().GetCoatRoughnessMinValue()

    @property
    def coatRoughness(self):
        return self.actor.GetProperty().GetCoatRoughness()

    @coatRoughness.setter
    def coatRoughness(self, value):
        self.actor.GetProperty().SetCoatRoughness(value)

    # =========== Emissive ======================================================
    @property
    def emissiveFactor(self):
        return self.actor.GetProperty().GetEmissiveFactor()

    @emissiveFactor.setter
    def emissiveFactor(self, value):
        self.actor.GetProperty().SetEmissiveFactor(value)

    @property
    def emissiveTexture(self):
        return self.actor.GetProperty().GetTexture("emissiveTexture")

    @emissiveTexture.setter
    def emissiveTexture(self, value):
        self.actor.GetProperty().SetEmissiveTexture(value)

    # =========== Normal ======================================================
    @property
    def normalScale(self):
        return self.actor.GetProperty().GetNormalScale()

    @normalScale.setter
    def normalScale(self, value):
        self.actor.GetProperty().SetNormalScale(value)

    @property
    def normalTexture(self):
        return self.actor.GetProperty().GetTexture("normalTexture")

    @normalTexture.setter
    def normalTexture(self, value):
        self.actor.GetProperty().SetNormalTexture(value)

    # =========== Metallic ======================================================
    @property
    def metallicMax(self):
        return self.actor.GetProperty().GetMetallicMaxValue()

    @property
    def metallicMin(self):
        return self.actor.GetProperty().GetMetallicMinValue()

    @property
    def metallic(self):
        return self.actor.GetProperty().GetMetallic()

    @metallic.setter
    def metallic(self, value):
        self.actor.GetProperty().SetMetallic(value)

    # =========== Roughness ======================================================
    @property
    def roughnessMax(self):
        return self.actor.GetProperty().GetRoughnessMaxValue()

    @property
    def roughnessMin(self):
        return self.actor.GetProperty().GetRoughnessMinValue()

    @property
    def roughness(self):
        return self.actor.GetProperty().GetRoughness()

    @roughness.setter
    def roughness(self, value):
        self.actor.GetProperty().SetRoughness(value)

    # =========== OcclusionStrength ======================================================
    @property
    def occlusionStrengthMax(self):
        return self.actor.GetProperty().GetOcclusionStrengthMaxValue()

    @property
    def occlusionStrengthMin(self):
        return self.actor.GetProperty().GetOcclusionStrengthMinValue()

    @property
    def occlusionStrength(self):
        return self.actor.GetProperty().GetOcclusionStrength()

    @occlusionStrength.setter
    def occlusionStrength(self, value):
        self.actor.GetProperty().SetOcclusionStrength(value)

    # =========== Edge ======================================================
    @property
    def edgeTint(self):
        return self.actor.GetProperty().GetEdgeTint()

    @edgeTint.setter
    def edgeTint(self, value):
        self.actor.GetProperty().SetEdgeTint(value)

    @property
    def edgeColor(self):
        return self.actor.GetProperty().GetEdgeColor()

    @edgeColor.setter
    def edgeColor(self, value):
        self.actor.GetProperty().SetEdgeColor(value)

    @property
    def edgeOpacityMax(self):
        return self.actor.GetProperty().GetEdgeOpacityMaxValue()

    @property
    def edgeOpacityMin(self):
        return self.actor.GetProperty().GetEdgeOpacityMinValue()

    @property
    def edgeOpacity(self):
        return self.actor.GetProperty().GetEdgeOpacity()

    @edgeOpacity.setter
    def edgeOpacity(self, value):
        self.actor.GetProperty().SetEdgeOpacity(value)

    @property
    def edgeVisibility(self):
        return self.actor.GetProperty().GetEdgeVisibility()

    @edgeVisibility.setter
    def edgeVisibility(self, value):
        self.actor.GetProperty().SetEdgeVisible(value)

    # =========== Line ======================================================
    @property
    def lineWidthMax(self):
        return self.actor.GetProperty().GetLineWidthMaxValue()

    @property
    def lineWidthMin(self):
        return self.actor.GetProperty().GetLineWidthMinValue()

    @property
    def lineWidth(self):
        return self.actor.GetProperty().GetLineWidth()

    @lineWidth.setter
    def lineWidth(self, value):
        self.actor.GetProperty().SetLineWidth(value)

    @property
    def lineStippleRepeatFactorMax(self):
        return self.actor.GetProperty().GetLineStippleRepeatFactorMaxValue()

    @property
    def lineStippleRepeatFactorMin(self):
        return self.actor.GetProperty().GetLineStippleRepeatFactorMinValue()

    @property
    def lineStippleRepeatFactor(self):
        return self.actor.GetProperty().GetLineStippleRepeatFactor()

    @lineStippleRepeatFactor.setter
    def lineStippleRepeatFactor(self, value):
        self.actor.GetProperty().SetLineStippleRepeatFactor(value)

    @property
    def lineStipplePattern(self):
        return self.actor.GetProperty().GetLineStipplePattern()

    @lineStipplePattern.setter
    def lineStipplePattern(self, value):
        self.actor.GetProperty().SetLineStipplePattern(value)

    # =========== Vertex ======================================================
    @property
    def vertexColor(self):
        return self.actor.GetProperty().GetVertexColor()

    @vertexColor.setter
    def vertexColor(self, value):
        self.actor.GetProperty().SetVertexColor(value)

    @property
    def vertexVisibility(self):
        return self.actor.GetProperty().GetVertexVisibility()

    @vertexVisibility.setter
    def vertexVisibility(self, value):
        self.actor.GetProperty().SetVertexVisibility(value)

    # =========== Point ======================================================
    @property
    def pointSizeMax(self):
        return self.actor.GetProperty().GetPointSizeMaxValue()

    @property
    def pointSizeMin(self):
        return self.actor.GetProperty().GetPointSizeMinValue()

    @property
    def pointSize(self):
        return self.actor.GetProperty().GetPointSize()

    @pointSize.setter
    def pointSize(self, value):
        self.actor.GetProperty().SetPointSize(value)

    # =========== ORM ======================================================
    @property
    def ORMTexture(self):
        return self.actor.GetProperty().GetTexture("ORMTexture")

    @ORMTexture.setter
    def ORMTexture(self, value):
        self.actor.GetProperty().SetORMTexture(value)

    # =========== Opacity ======================================================
    @property
    def opacityMax(self):
        return self.actor.GetProperty().GetOpacityMaxValue()

    @property
    def opacityMin(self):
        return self.actor.GetProperty().GetOpacityMinValue()

    @property
    def opacity(self):
        return self.actor.GetProperty().GetOpacity()

    @opacity.setter
    def opacity(self, value):
        self.actor.GetProperty().SetOpacity(value)

    # =========== Culling ======================================================
    @property
    def backFaceCulling(self):
        return self.actor.GetProperty().GetBackfaceCulling()

    @backFaceCulling.setter
    def backFaceCulling(self, value):
        self.actor.GetProperty().SetBackfaceCulling(value)

    @property
    def frontFaceCulling(self):
        return self.actor.GetProperty().GetFrontfaceCulling()

    @frontFaceCulling.setter
    def frontFaceCulling(self, value):
        self.actor.GetProperty().SetFrontfaceCulling(value)

    @property
    def showTexturesOnBackface(self):
        return self.actor.GetProperty().GetShowTexturesOnBackface()

    @showTexturesOnBackface.setter
    def showTexturesOnBackface(self, value):
        self.actor.GetProperty().SetShowTexturesOnBackface(value)

    # =========== Interpolation ======================================================
    @property
    def interpolationMax(self):
        return self.actor.GetProperty().GetInterpolationMaxValue()

    @property
    def interpolationMin(self):
        return self.actor.GetProperty().GetInterpolationMinValue()

    @property
    def interpolation(self):
        return self.actor.GetProperty().GetInterpolation()

    def interpolationString(self):
        return self.actor.GetProperty().GetInterpolationAsString()

    @interpolation.setter
    def interpolation(self, value):
        self.actor.GetProperty().SetInterpolation(value)

    # =========== Representation ======================================================
    @property
    def representationMax(self):
        return self.actor.GetProperty().GetRepresentationMaxValue()

    @property
    def representationMin(self):
        return self.actor.GetProperty().GetRepresentationMinValue()

    @property
    def representation(self):
        return self.actor.GetProperty().GetRepresentation()

    def representationString(self):
        return self.actor.GetProperty().GetRepresentationAsString()

    @representation.setter
    def representation(self, value):
        self.actor.GetProperty().SetRepresentation(value)

    # =========== Render Present ======================================================
    @property
    def renderPointsAsSpheres(self):
        return self.actor.GetProperty().GetRenderPointsAsSpheres()

    @renderPointsAsSpheres.setter
    def renderPointsAsSpheres(self, value):
        self.actor.GetProperty().SetRenderPointsAsSpheres(value)

    @property
    def renderLinesAsTubes(self):
        return self.actor.GetProperty().GetRenderLinesAsTubes()

    @renderLinesAsTubes.setter
    def renderLinesAsTubes(self, value):
        self.actor.GetProperty().SetRenderLinesAsTubes(value)

    # =========== Selection ======================================================
    @property
    def selectionColor(self):
        return self.actor.GetProperty().GetSelectionColor()

    @selectionColor.setter
    def selectionColor(self, value):
        self.actor.GetProperty().SetSelectionColor(value)

    @property
    def selectionLineWidth(self):
        return self.actor.GetProperty().GetSelectionLineWidth()

    @selectionLineWidth.setter
    def selectionLineWidth(self, value):
        self.actor.GetProperty().SetSelectionLineWidth(value)

    @property
    def selectionPointSize(self):
        return self.actor.GetProperty().GetSelectionPointSize()

    @selectionPointSize.setter
    def selectionPointSize(self, value):
        self.actor.GetProperty().SetSelectionPointSize(value)

    # =========== Mapper ======================================================
    @property
    def mapper(self):
        return self.actor.GetMapper()

    @mapper.setter
    def mapper(self, value):
        self.actor.SetMapper(value)
