import FreeCAD
import Part as PartModule
import Part.Geom2d


# BuildPlateSurfacePy.xml
class BuildPlateSurfacePy(FreeCAD.PyObjectBase):
    """This class provides an algorithm for constructing such a plate surface."""

    def __init__(self, Surface: PartModule.GeometrySurface = None, Degree: int = 3, NbPtsOnCur: int = 10, NbIter: int = 3, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1, Anisotropy: bool = False):
        """
        This class provides an algorithm for constructing such a plate surface.
        Possible exceptions: (ReferenceError, RuntimeError).
        """

    def G0Error(self, index: int = 0, /) -> float:
        """
        Returns the max distance between the result and the constraints
        Possible exceptions: (RuntimeError).
        """

    def G1Error(self, index: int = 0, /) -> float:
        """
        Returns the max angle between the result and the constraints
        Possible exceptions: (RuntimeError).
        """

    def G2Error(self, index: int = 0, /) -> float:
        """
        Returns the max difference of curvature between the result and the constraints
        Possible exceptions: (RuntimeError).
        """

    def add(self, cont, /):
        """
        Adds a linear or point constraint
        Possible exceptions: (TypeError, RuntimeError).
        """

    def curveConstraint(self, index: int, /) -> PartModule.CurveConstraint:
        """
        Returns the curve constraint of order
        Possible exceptions: (RuntimeError).
        """

    def curves2d(self) -> list[PartModule.Geom2d.Curve2d]:
        """
        Extracts the array of curves on the plate surface which
                correspond to the curve constraints set in add()
        
        Possible exceptions: (RuntimeError).
        """

    def disc2dContour(self, index: int, /) -> list[tuple[float, float]]:
        """Possible exceptions: (RuntimeError)."""

    def disc3dContour(self, index: int, order: int, /) -> list[tuple[float, float, float]]:
        """Possible exceptions: (RuntimeError)."""

    def init(self):
        """
        Resets all constraints
        Possible exceptions: (RuntimeError).
        """

    def isDone(self) -> bool:
        """
        Tests whether computation of the plate has been completed
        Possible exceptions: (RuntimeError).
        """

    def loadInitSurface(self, surf: PartModule.GeometrySurface, /):
        """
        Loads the initial surface
        Possible exceptions: (ReferenceError, RuntimeError).
        """

    def order(self) -> list[int]:
        """
        Returns the order of the curves in the array returned by curves2d
        Possible exceptions: (RuntimeError).
        """

    def perform(self):
        """
        Calls the algorithm and computes the plate surface
        Possible exceptions: (RuntimeError).
        """

    def pointConstraint(self, index: int, /) -> PartModule.PointConstraint:
        """
        Returns the point constraint of order
        Possible exceptions: (RuntimeError).
        """

    def sense(self) -> list[int]:
        """
        Returns the orientation of the curves in the array returned by curves2d
        Possible exceptions: (RuntimeError).
        """

    def setNbBounds(self, count: int, /):
        """Possible exceptions: (RuntimeError)."""

    def surfInit(self) -> PartModule.GeometrySurface:
        """
        Returns the initial surface
        Possible exceptions: (RuntimeError).
        """

    def surface(self) -> PartModule.GeometrySurface:
        """
        Returns the plate surface
        Possible exceptions: (RuntimeError).
        """


# CurveConstraintPy.xml
class CurveConstraintPy(FreeCAD.PyObjectBase):
    """Defines curves as constraints to be used to deform a surface"""

    def __init__(self, Boundary: PartModule.Curve, Order: int = 0, NbPts: int = 10, TolDist: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1):
        """
        Defines curves as constraints to be used to deform a surface
        Possible exceptions: (ReferenceError, RuntimeError).
        """

    @property
    def FirstParameter(self) -> float:
        """
        This function returns the first parameter of the curve.
        The first parameter is the lowest parametric value for the curve, which defines the starting point of the curve.
        Possible exceptions: (RuntimeError).
        """

    @property
    def LastParameter(self) -> float:
        """
        This function returns the last parameter of the curve.
        The last parameter is the highest parametric value for the curve, which defines the ending point of the curve.
        Possible exceptions: (RuntimeError).
        """

    @property
    def Length(self) -> float:
        """
        This function returns the length of the curve.
        The length of the curve is a geometric property that indicates how long the curve is in the space.
        Possible exceptions: (RuntimeError).
        """

    @property
    def NbPoints(self) -> int:
        """
        The number of points on the curve used as a
        constraint. The default setting is 10. This parameter
        affects computation time, which increases by the cube of
        the number of points.
        Possible exceptions: (RuntimeError).
        """

    def G0Criterion(self, u: float, /) -> float:
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        
        Possible exceptions: (RuntimeError).
        """

    def G1Criterion(self, u: float, /) -> float:
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def G2Criterion(self, u: float, /) -> float:
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def curve2dOnSurf(self) -> PartModule.Geom2d.Curve2d:
        """
        Returns a 2d curve associated the surface resulting of the constraints
        Possible exceptions: (RuntimeError).
        """

    def curve3d(self):
        """
        Returns a 3d curve associated the surface resulting of the constraints
        Possible exceptions: (RuntimeError).
        """

    def order(self) -> int:
        """
        Returns the order of constraint, one of G0, G1 or G2
        Possible exceptions: (RuntimeError).
        """

    def projectedCurve(self):
        """
        Returns the projected curve resulting from the normal projection of the
         curve on the initial surface
        Possible exceptions: (RuntimeError).
        """

    def setCurve2dOnSurf(self, c: PartModule.Curve2d, /):
        """
        loads a 2d curve associated the surface resulting of the constraints

        Possible exceptions: (ReferenceError, RuntimeError).
        """

    def setG0Criterion(self):
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
        
        Possible exceptions: (NotImplementedError).
        """

    def setG1Criterion(self):
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises an exception if  the  curve  is  not  on  a  surface
        
        Possible exceptions: (NotImplementedError).
        """

    def setG2Criterion(self):
        """
        Allows you to set the G2 criterion. This is the law
         defining the greatest difference in curvature allowed
         between the constraint and the target surface. If this
         criterion is not set, TolCurv, the curvature tolerance from
         the constructor, is used.
         Raises   ConstructionError if  the  point  is  not  on  the  surface
        
        Possible exceptions: (NotImplementedError).
        """

    def setOrder(self, order: int, /):
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        
        Possible exceptions: (RuntimeError).
        """

    def setProjectedCurve(self, c: PartModule.Curve2d, tolU: float, tolV: float, /):
        """
        loads a 2d curve  resulting from the normal projection of
         the curve on the initial surface
        Possible exceptions: (ReferenceError, RuntimeError).
        """


# PointConstraintPy.xml
class PointConstraintPy(FreeCAD.PyObjectBase):
    """Defines points as constraints to be used to deform a surface"""

    def __init__(self, Point: FreeCAD.Vector, Order: int = 0, TolDist: float = 0.0001):
        """
        Defines points as constraints to be used to deform a surface
        Possible exceptions: (RuntimeError).
        """

    def G0Criterion(self) -> float:
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        
        Possible exceptions: (RuntimeError).
        """

    def G1Criterion(self) -> float:
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def G2Criterion(self) -> float:
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises an exception if  the  curve  is  not  on  a  surface.
        
        Possible exceptions: (RuntimeError).
        """

    def hasPnt2dOnSurf(self) -> bool:
        """
        Checks if there is a 2D point associated with the surface. It returns a boolean indicating whether such a point exists.
        Possible exceptions: (RuntimeError).
        """

    def order(self) -> int:
        """
        Returns the order of constraint, one of G0, G1 or G2
        Possible exceptions: (RuntimeError).
        """

    def pnt2dOnSurf(self) -> tuple[float, float]:
        """
        Returns the 2D point on the surface. It returns a gp_Pnt2d representing the associated 2D point.
        Possible exceptions: (RuntimeError).
        """

    def setG0Criterion(self, tolDist: float, /):
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
        
        Possible exceptions: (RuntimeError).
        """

    def setG1Criterion(self, tolAng: float, /):
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises an exception if  the  curve  is  not  on  a  surface
        
        Possible exceptions: (RuntimeError).
        """

    def setG2Criterion(self, tolCurv: float, /):
        """
        Allows you to set the G2 criterion. This is the law
         defining the greatest difference in curvature  allowed between the
         constraint and the target surface. If this criterion is not
         set, TolCurv, the curvature tolerance from the constructor, is used.
         Raises  ConstructionError if  the  curve  is  not  on  a  surface
        Possible exceptions: (RuntimeError).
        """

    def setOrder(self, order: int, /):
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        
        Possible exceptions: (RuntimeError).
        """

    def setPnt2dOnSurf(self, x: float, y: float, /):
        """
        Allows you to set a 2D point on the surface. It takes a gp_Pnt2d as an argument, representing the 2D point to be associated with the surface.
        Possible exceptions: (RuntimeError).
        """
