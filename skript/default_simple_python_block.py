from __future__ import annotations

import numpy as np

from textwrap import dedent
from typing import TYPE_CHECKING, Dict, Optional

from flower.base.interfaces import \
    UserPortIn, UserParameter, UserPortOut, UserProperty
from flower.blocks.dataflow_python_blocks import SimplePythonDataflowBlock





#### 1 формула (1)
DEFAULT_CALC_SOURCE_SPACE_TIME = dedent(
    '''
    import numpy as np

    период_обзора_пространства = (сектор_обзора_по_азимуту / шаг_перемещения_по_азимуту + 1) * ((угол_места_макс - угол_места_мин)/ шаг_перемещения_по_углу_места +1) * количество_зондирующих_сигналов_в_одном_направлении * период_повторения_зондирующих_сигналов
    '''
)


class SpaceTime(SimplePythonDataflowBlock):
    сектор_обзора_по_азимуту = UserPortIn()
    шаг_перемещения_по_азимуту = UserPortIn()
    разрешающая_способность = UserPortIn()
    угол_места_макс = UserPortIn()
    угол_места_мин = UserPortIn()
    шаг_перемещения_по_углу_места = UserPortIn()
    количество_зондирующих_сигналов_в_одном_направлении = UserPortIn()
    период_повторения_зондирующих_сигналов = UserPortIn()

    период_обзора_пространства = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SPACE_TIME):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 2 формула (2)
DEFAULT_CALC_SOURCE_REPEAT_SIGNALS = dedent(
    '''
    import numpy as np

    период_повторения_зондирующих_сигналов = 2 * требуемая_максимальная_дальность_обнаружения / скорость_света
    '''
)


class RepeatSignals(SimplePythonDataflowBlock):
    требуемая_максимальная_дальность_обнаружения = UserPortIn()
    скорость_света = UserPortIn()
 
    период_повторения_зондирующих_сигналов = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_REPEAT_SIGNALS):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 3 формула (3)
DEFAULT_CALC_SOURCE_MAXIMUM_RANGE_OF_DETECTING = dedent(
    '''
    import numpy as np

    максимальная_реализуемая_дальность_обнаружения_цели = (потенциал_РЛС * ЭПР_цели / значение_фиксированного_порога_обнаружения) ** (1/4)   '''
)


class MaximumRangeOfDetecting(SimplePythonDataflowBlock):
    потенциал_РЛС = UserPortIn()
    ЭПР_цели = UserPortIn()
    значение_фиксированного_порога_обнаружения = UserPortIn()

    максимальная_реализуемая_дальность_обнаружения_цели = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_MAXIMUM_RANGE_OF_DETECTING):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 4 формула (4)
DEFAULT_CALC_SOURCE_THRESHOLD_DETECTING = dedent(
    '''
    import numpy as np

    значение_фиксированного_порога_обнаружения = (1/(количество_импульсов_в_пачке ** коэффициент_когерентности) * ( np.log10(заданная_вероятность_ложной_тревоги)/np.log10(заданная_вероятность_правильного_обнаружения) - 1 )) ** (1/2)   '''
)


class ThresholdDetecting(SimplePythonDataflowBlock):
    количество_импульсов_в_пачке = UserPortIn()
    коэффициент_когерентности = UserPortIn()
    значение_фиксированного_порога_обнаружения = UserPortIn()
    заданная_вероятность_ложной_тревоги = UserPortIn()
    заданная_вероятность_правильного_обнаружения = UserPortIn()

    значение_фиксированного_порога_обнаружения = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_THRESHOLD_DETECTING):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


####  формула между 4 и 5 (5)
DEFAULT_CALC_SOURCE_NUMBER_IMPULSES = dedent(
    '''
    import numpy as np

    количество_импульсов_в_пачке = 1 + (ширина_ДНА_в_горизонтальной_плоскости_по_половинной_мощности * период_повторения_зондирующих_сигналов)// скорость_кругового_вращения_антенны
    '''
)


class NumberImpulses(SimplePythonDataflowBlock):
             
    ширина_ДНА_в_горизонтальной_плоскости_по_половинной_мощности = UserPortIn()
    период_повторения_зондирующих_сигналов = UserPortIn()
    скорость_кругового_вращения_антенны = UserPortIn()
   
    количество_импульсов_в_пачке = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_NUMBER_IMPULSES):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 5 формула (6)
DEFAULT_CALC_SOURCE_REQUIRED_RADAR_POTENTIAL = dedent(
    '''
    import numpy as np

    требуемый_потенциал_РЛС = требуемая_максимальная_дальность_обнаружения ** 4 * значение_фиксированного_порога_обнаружения / ЭПР_цели
    '''
)


class RequiredRadarPotential(SimplePythonDataflowBlock):
             
    требуемая_максимальная_дальность_обнаружения = UserPortIn()
    значение_фиксированного_порога_обнаружения = UserPortIn()
    ЭПР_цели = UserPortIn()
   
    требуемый_потенциал_РЛС = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_REQUIRED_RADAR_POTENTIAL):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 6 формула (7)
DEFAULT_CALC_SOURCE_RADAR_POTENTIAL = dedent(
    '''
    import numpy as np

    потенциал_РЛС = (импульсная_мощность_передатчика * коэффициент_усиления_передающей_антенны * коэффициент_усиления_приемной_антенны * длина_волны ** 2 * суммарный_коэффициент_потерь_в_приемном_тракте_антенны * значение_нормированной_диаграммы_направленности_передающей_антенны_РЛС * значение_нормированной_диаграммы_направленности_принимающей_антенны_РЛС) / ((4 * np.pi ) ** 3 * чувствительность_приемника )
    '''
)


class RadarPotential(SimplePythonDataflowBlock):
             
    импульсная_мощность_передатчика = UserPortIn()
    коэффициент_усиления_передающей_антенны = UserPortIn()
    коэффициент_усиления_приемной_антенны = UserPortIn()
    длина_волны = UserPortIn()
    суммарный_коэффициент_потерь_в_приемном_тракте_антенны = UserPortIn()
    значение_нормированной_диаграммы_направленности_передающей_антенны_РЛС = UserPortIn()
    значение_нормированной_диаграммы_направленности_принимающей_антенны_РЛС = UserPortIn()
    чувствительность_приемника = UserPortIn()


    потенциал_РЛС = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_RADAR_POTENTIAL):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 7 формула (8)
DEFAULT_CALC_SOURCE_SENSITY = dedent(
    '''
    import numpy as np

    чувствительность_приемника = постоянная_Больцмана * коэффициент_шума_приемника * температура * полоса_пропускания_приемного_устройства
    '''
)


class Sensity(SimplePythonDataflowBlock):
             
    коэффициент_шума_приемника = UserPortIn()
    полоса_пропускания_приемного_устройства = UserPortIn()
    температура = UserPortIn()
    постоянная_Больцмана = UserPortIn()

    чувствительность_приемника = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SENSITY):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 8 формула (9)
DEFAULT_CALC_SOURCE_ANTENNA_GAIN_MY = dedent(
    '''
    import numpy as np
    
    коэффициент_усиления_антенны = 4 * np.pi * эффективная_площадь_раскрыва_антенны / (длина_волны ** 2)
    '''
)


class AntennaGainMy(SimplePythonDataflowBlock):
             
    эффективная_площадь_раскрыва_антенны = UserPortIn()
    длина_волны = UserPortIn()

    коэффициент_усиления_антенны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_GAIN_MY):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 9 формула (10)
DEFAULT_CALC_SOURCE_ANTENNA_GAIN_WITH_KPD = dedent(
    '''
    import numpy as np
    
    коэффициент_усиления_антенны = 4 * np.pi * КПД_антенного_тракта * эффективная_площадь_раскрыва_антенны / (длина_волны ** 2)
    '''
)


class AntennaGainWithKpd(SimplePythonDataflowBlock):
             
    эффективная_площадь_раскрыва_антенны = UserPortIn()
    длина_волны = UserPortIn()
    КПД_антенного_тракта = UserPortIn()

    коэффициент_усиления_антенны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_GAIN_WITH_KPD):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 11 формула (11)
DEFAULT_CALC_SOURCE_POTENTIAL_LONG = dedent(
    '''
    import numpy as np

    потенциал_РЛС_через_пост_Больцмана = импульсная_мощность_передатчика * длительность_импульса * эффективная_площадь_раскрыва_передающей_антенны * эффективная_площадь_раскрыва_приемной_антенны * суммарный_коэффициент_потерь_в_приемном_тракте_антенны * значение_нормированной_диаграммы_направленности_передающей_антенны_РЛС * значение_нормированной_диаграммы_направленности_принимающей_антенны_РЛС) / (4 * np.pi * длина_волны ** 2 * постоянная_Больцмана * коэффициент_шума_приемника * температура)
    '''
)

#
# class PotentialLong(SimplePythonDataflowBlock):
#
#     импульсная_мощность_передатчика = UserPortIn()
#     длительность_импульса = UserPortIn()
#     эффективная_площадь_раскрыва_передающей_антенны = UserPortIn()
#     эффективная_площадь_раскрыва_приемной_антенны = UserPortIn()
#     суммарный_коэффициент_потерь_в_приемном_тракте_антенны = UserPortIn()
#     значение_нормированной_диаграммы_направленности_передающей_антенны_РЛС = UserPortIn()
#     значение_нормированной_диаграммы_направленности_принимающей_антенны_РЛС = UserPortIn()
#     длина_волны = UserPortIn()
#     коэффициент_шума_приемника = UserPortIn()
#     постоянная_Больцмана = UserPortIn()
#     температура = UserPortIn()
#
#     потенциал_РЛС_через_пост_Больцмана = UserPortOut()
#
#     def __init__(self, id: Optional[str] = None, *,
#                  user_parameters: Optional[Dict[str, UserParameter]] = None,
#                  user_properties: Optional[Dict[str, UserProperty]] = None,
#                  user_in_ports: Optional[Dict[str, UserPortIn]] = None,
#                  user_out_ports: Optional[Dict[str, UserPortOut]] = None,
#                  init_source: str = '',
#                  calc_source: str = DEFAULT_CALC_SOURCE_POTENTIAL_LONG):
#         super().__init__(id=id,
#                          user_parameters=user_parameters,
#                          user_properties=user_properties,
#                          user_in_ports=user_in_ports,
#                          user_out_ports=user_out_ports,
#                          init_source=init_source,
#                          calc_source=calc_source)
#


#### 12 формула (12)
DEFAULT_CALC_SOURCE_SQUARE_PASS = dedent(
    '''
    import numpy as np

    эффективная_площадь_передающей_антенны = апертура_передающей_антенны_РЛС_в_горизонтальной_плоскости * апертура_передающей_антенны_РЛС_в_вертикальной_плоскости * коэффициент_использования_геометрической_площади
    '''
)


class SquarePass(SimplePythonDataflowBlock):
             
    апертура_передающей_антенны_РЛС_в_горизонтальной_плоскости = UserPortIn()
    апертура_передающей_антенны_РЛС_в_вертикальной_плоскости = UserPortIn()
    коэффициент_использования_геометрической_площади = UserPortIn()

    эффективная_площадь_передающей_антенны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SQUARE_PASS):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 13 формула (13)
DEFAULT_CALC_SOURCE_SQUARE_TAKE = dedent(
    '''
    import numpy as np

    эффективная_площадь_приемной_антенны = апертура_приемной_антенны_РЛС_в_горизонтальной_плоскости * апертура_приемной_антенны_РЛС_в_вертикальной_плоскости * коэффициент_использования_геометрической_площади
    '''
)


class SquareTake(SimplePythonDataflowBlock):
             
    апертура_приемной_антенны_РЛС_в_горизонтальной_плоскости = UserPortIn()
    апертура_приемной_антенны_РЛС_в_вертикальной_плоскости = UserPortIn()
    коэффициент_использования_геометрической_площади = UserPortIn()

    эффективная_площадь_приемной_антенны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SQUARE_TAKE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 14 формула (14)
DEFAULT_CALC_SOURCE_ANTENNA_ANGLE_APERTURE = dedent(
    '''
    import numpy as np

    апертура_антенны_по_углу_альфа = (количество_излучателей_в_линии_по_углу_альфа - 1) * расстояние_облучателей_друг_от_друга
    '''
)


class AntennaAngleAperture(SimplePythonDataflowBlock):
             
    количество_излучателей_в_линии_по_углу_альфа = UserPortIn()
    расстояние_облучателей_друг_от_друга = UserPortIn()

    апертура_антенны_по_углу_альфа = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_ANGLE_APERTURE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 15 формула (15)
DEFAULT_CALC_SOURCE_SUMMARY_IMPULSE_POWER = dedent(
    '''
    import numpy as np

    суммарная_импульсная_мощность_РЛС = импульсная_мощность_одного_канала_ФАР * общее_количество_передающих_каналов_ФАР
    '''
)


class SummaryImpulsePower(SimplePythonDataflowBlock):
             
    импульсная_мощность_одного_канала_ФАР = UserPortIn()
    общее_количество_передающих_каналов_ФАР = UserPortIn()

    суммарная_импульсная_мощность_РЛС = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SUMMARY_IMPULSE_POWER):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 17 (1)  (17)
DEFAULT_CALC_SOURCE_CRUSHING_RATIO_PASS = dedent(
    '''
    import numpy as np

    коэффициент_дробления_передающего_полотна_антенны_РЛС = работающее_количество_передающих_СВЧ_каналов / номинальное_количество_передающих_СВЧ_каналов
    '''
)


class CrushingRatioPass(SimplePythonDataflowBlock):
             
    работающее_количество_передающих_СВЧ_каналов = UserPortIn()
    номинальное_количество_передающих_СВЧ_каналов = UserPortIn()

    коэффициент_дробления_передающего_полотна_антенны_РЛС = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_CRUSHING_RATIO_PASS):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 17 (2)  (18)
DEFAULT_CALC_SOURCE_CRUSHING_RATIO_TAKE = dedent(
    '''
    import numpy as np

    коэффициент_дробления_приемного_полотна_антенны_РЛС = работающее_количество_приемных_СВЧ_каналов / номинальное_количество_приемных_СВЧ_каналов
    '''
)


class CrushingRatioTake(SimplePythonDataflowBlock):
             
    работающее_количество_приемных_СВЧ_каналов = UserPortIn()
    номинальное_количество_приемных_СВЧ_каналов = UserPortIn()

    коэффициент_дробления_приемного_полотна_антенны_РЛС = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_CRUSHING_RATIO_TAKE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

##### 18 (19)
DEFAULT_CALC_SOURCE_ANTENNA_PATTERN = dedent(
    '''
    import numpy as np
    
    ДНА = np.exp(-np.pi* ((угловые_координаты_выставления_луча_ДНА - угловые_координаты_цели) / ширина_ДНА_по_половинной_мощности) ** 2 )
    '''
)
class AntennaPattern(SimplePythonDataflowBlock):
             
    угловые_координаты_выставления_луча_ДНА = UserPortIn()      
    угловые_координаты_цели = UserPortIn() 
    ширина_ДНА_по_половинной_мощности = UserPortIn()      

    ДНА = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_PATTERN):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 19 (20)
DEFAULT_CALC_SOURCE_BEAM_WIDTH = dedent(
    '''
    import numpy as np

    ширина_луча_по_точкам_половинной_мощности = коэффициент_расширения_главного_лепестка_ДНА * длина_волны  / (апертура_антенны_по_углу_альфа * np.cos(азимут_или_угол_места_нормали_к_полотну_антенны_РЛС - азимут_или_угол_места_выставления_луча_ДНА) )
    '''
)


class BeamWidth(SimplePythonDataflowBlock):
             
    коэффициент_расширения_главного_лепестка_ДНА = UserPortIn()
    длина_волны = UserPortIn()      
    апертура_антенны_по_углу_альфа = UserPortIn()
    азимут_или_угол_места_нормали_к_полотну_антенны_РЛС = UserPortIn()
    азимут_или_угол_места_выставления_луча_ДНА = UserPortIn()

    ширина_луча_по_точкам_половинной_мощности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_BEAM_WIDTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 20 (21)
DEFAULT_CALC_SOURCE_DNA_FLAT_FAR = dedent(
    '''
    import numpy as np

    ДНА_плоской_ФАР = np.sin(количество_излучателей_в_линии_по_углу_альфа * np.pi * (расстояние_облучателей_друг_от_друга / длина_волны) * (np.sin(азимут_или_угол_места_выставления_луча_ДНА - альфа) - np.sin(азимут_или_угол_места_нормали_к_полотну_антенны_РЛС - азимут_или_угол_места_выставления_луча_ДНА)))**2 / (количество_излучателей_в_линии_по_углу_альфа ** 2 * np.sin( * np.pi * (расстояние_облучателей_друг_от_друга / длина_волны) * (np.sin(азимут_или_угол_места_выставления_луча_ДНА - альфа) - np.sin(азимут_или_угол_места_нормали_к_полотну_антенны_РЛС - азимут_или_угол_места_выставления_луча_ДНА)))**2
'''
)

#
# class DnaFlatFar(SimplePythonDataflowBlock):
#
#     количество_излучателей_в_линии_по_углу_альфа = UserPortIn()
#     расстояние_облучателей_друг_от_друга = UserPortIn()
#     длина_волны = UserPortIn()
#     азимут_или_угол_места_выставления_луча_ДНА = UserPortIn()
#     альфа = UserPortIn()
#     азимут_или_угол_места_нормали_к_полотну_антенны_РЛС = UserPortIn()
#     альфа = UserPortIn()
#
#     ДНА_плоской_ФАР = UserPortOut()
#
#     def __init__(self, id: Optional[str] = None, *,
#                  user_parameters: Optional[Dict[str, UserParameter]] = None,
#                  user_properties: Optional[Dict[str, UserProperty]] = None,
#                  user_in_ports: Optional[Dict[str, UserPortIn]] = None,
#                  user_out_ports: Optional[Dict[str, UserPortOut]] = None,
#                  init_source: str = '',
#                  calc_source: str = DEFAULT_CALC_SOURCE_DNA_FLAT_FAR):
#         super().__init__(id=id,
#                          user_parameters=user_parameters,
#                          user_properties=user_properties,
#                          user_in_ports=user_in_ports,
#                          user_out_ports=user_out_ports,
#                          init_source=init_source,
#                          calc_source=calc_source)


#### 21 (22)
DEFAULT_CALC_SOURCE_SIGNAL_TO_NOISE_RATIO = dedent(
    '''
    import numpy as np

    отношение_сигнал_шум = потенциал_РЛС * ЭПР_цели / (требуемый_рубеж_обнаружения ** 4)
    '''
)


class SignalToNoiseRatio(SimplePythonDataflowBlock):
             
    потенциал_РЛС = UserPortIn()
    ЭПР_цели = UserPortIn()      
    требуемый_рубеж_обнаружения = UserPortIn()

    отношение_сигнал_шум = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SIGNAL_TO_NOISE_RATIO):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 22 (23)
DEFAULT_CALC_SOURCE_PROBABILITY_OF_DETECTION = dedent(
    '''
    import numpy as np

    вероятность_обнаружения_цели_на_заданном_рубеже_1 = np.exp(np.log10(заданная_вероятность_ложной_тревоги)/ (отношение_сигнал_шум ** 2 + 1))
    '''
)


class ProbabilityOfDetection(SimplePythonDataflowBlock):
             
    заданная_вероятность_ложной_тревоги = UserPortIn()
    отношение_сигнал_шум = UserPortIn()      

    вероятность_обнаружения_цели_на_заданном_рубеже_1 = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_PROBABILITY_OF_DETECTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 23 (24)
DEFAULT_CALC_SOURCE_PROBABILITY_DETECTION = dedent(
    '''
    import numpy as np

    вероятность_обнаружения_цели_на_заданном_рубеже_2 = np.exp(-(требуемый_рубеж_обнаружения /требуемая_максимальная_дальность_обнаружения)**4)
    '''
)


class ProbabilityDetection(SimplePythonDataflowBlock):
             
    требуемый_рубеж_обнаружения = UserPortIn()
    требуемая_максимальная_дальность_обнаружения = UserPortIn()      

    вероятность_обнаружения_цели_на_заданном_рубеже_2 = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_PROBABILITY_DETECTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 24 (25)
DEFAULT_CALC_SOURCE_ANGULAR_COORDINATE_AZIMUTH = dedent(
    '''
    import numpy as np

    СКО_угловой_координаты_по_азимуту = коэффициент_пропорциональности * длина_волны / (апертура_приемной_решетки_по_азимуту * np.cos(ориентация_нормали_к_полотну_приемной_антенны_РЛС - ориентация_максимума_диаграммы_направлености_приемного_луча) * отношение_сигнал_шум_по_мощности ** 0.5)
    '''
)


class AngularCoordinateAzimuth(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    длина_волны = UserPortIn()      
    апертура_приемной_решетки_по_азимуту = UserPortIn()
    ориентация_нормали_к_полотну_приемной_антенны_РЛС = UserPortIn()    
    ориентация_максимума_диаграммы_направлености_приемного_луча = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_угловой_координаты_по_азимуту = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_COORDINATE_AZIMUTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 25 (26)
DEFAULT_CALC_SOURCE_ANGULAR_COORDINATE_PLACE_ANGLE = dedent(
    '''
    import numpy as np

    СКО_угловой_координаты_по_углу_места = коэффициент_пропорциональности * длина_волны / (апертура_приемной_решетки_по_азимуту * np.cos(ориентация_нормали_к_полотну_приемной_антенны_РЛС - ориентация_максимума_диаграммы_направлености_приемного_луча) * отношение_сигнал_шум_по_мощности ** 0.5)
    '''
)


class AngularCoordinatePlaceAngle(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    длина_волны = UserPortIn()      
    апертура_приемной_решетки_по_азимуту = UserPortIn()
    ориентация_нормали_к_полотну_приемной_антенны_РЛС = UserPortIn()    
    ориентация_максимума_диаграммы_направлености_приемного_луча = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_угловой_координаты_по_углу_места = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_COORDINATE_PLACE_ANGLE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 28(1)  (27)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_UNMODULATED = dedent(
    '''
    import numpy as np

    СКО_измерения_дальности_немодулированный = коэффициент_пропорциональности * длительность_импульса * скорость_света / (отношение_сигнал_шум_по_мощности ** 0.5)
    '''
)


class StandartDeviationRangeUnmodulated(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    длительность_импульса = UserPortIn()      
    скорость_света = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_измерения_дальности_немодулированный = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_UNMODULATED):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 28(2)  (28)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_UNMODULATED_2 = dedent(
    '''
    import numpy as np

    СКО_измерения_дальности_немодулированный = коэффициент_пропорциональности * скорость_света / (отношение_сигнал_шум_по_мощности ** 0.5 * ширина_спектра_сигнала)
    '''
)


class StandartDeviationRangeUnmodulated2(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    ширина_спектра_сигнала = UserPortIn()      
    скорость_света = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_измерения_дальности_немодулированный = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_UNMODULATED_2):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 28(3) (29)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_VELOCITY_UNMODULATED = dedent(
    '''
    import numpy as np

    СКО_измерения_радиальной_скорости_немодулированный = коэффициент_пропорциональности * длина_волны / (отношение_сигнал_шум_по_мощности ** 0.5 * длительность_импульса)
    '''
)


class StandartDeviationVelocityUnmodulated(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    длина_волны = UserPortIn()      
    длительность_импульса = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_измерения_радиальной_скорости_немодулированный = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_VELOCITY_UNMODULATED):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 29(1) (30)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_LFM = dedent(
    '''
    import numpy as np

    СКО_измерения_дальности_ЛЧМ = коэффициент_пропорциональности * скорость_света / (отношение_сигнал_шум_по_мощности ** 0.5 * ширина_спектра_сигнала)
    '''
)


class StandartDeviationRangeLfm(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    ширина_спектра_сигнала = UserPortIn()      
    скорость_света = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_измерения_дальности_ЛЧМ = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_LFM):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 29(2) (31)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_VELOCITY_LFM = dedent(
    '''
    import numpy as np

    СКО_измерения_радиальной_скорости_ЛЧМ = 2 ** (0.5) * СКО_измерения_дальности / периодичность_излчуения_ЛЧМ_сигнала
    '''
)


class StandartDeviationVelocityLfm(SimplePythonDataflowBlock):
             
    СКО_измерения_дальности = UserPortIn()
    периодичность_излчуения_ЛЧМ_сигнала = UserPortIn()      

    СКО_измерения_радиальной_скорости_ЛЧМ = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_VELOCITY_LFM):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 30(1) (32)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_PHCM = dedent(
    '''
    import numpy as np

    СКО_измерения_дальности_ФКМ = коэффициент_пропорциональности * скорость_света *	длительность_дискрета_ФКМ_сигнала/ (отношение_сигнал_шум_по_мощности ** 0.5)
    '''
)


class StandartDeviationRangePhcm(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    скорость_света = UserPortIn()      
    длительность_дискрета_ФКМ_сигнала = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()    

    СКО_измерения_дальности_ФКМ = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_RANGE_PHCM):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 30(2) (33)
DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_VELOCITY_PHCM = dedent(
    '''
    import numpy as np

    СКО_измерения_радиальной_скорости_ФКМ = коэффициент_пропорциональности * длина_волны /	(длительность_импульса * отношение_сигнал_шум_по_мощности ** 0.5)
    '''
)


class StandartDeviationVelocityPhcm(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности = UserPortIn()
    длина_волны = UserPortIn()  
    длительность_импульса = UserPortIn()
    отношение_сигнал_шум_по_мощности = UserPortIn()          

    СКО_измерения_радиальной_скорости_ФКМ = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANGULAR_STANDART_DEVIATION_VELOCITY_PHCM):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)





#### 31 (34)
DEFAULT_CALC_SOURCE_HEIGHT_AIM = dedent(
    '''
    import numpy as np

    высота_цели =  наклонная_дальность_до_цели * np.sin(угол_места_цели) + наклонная_дальность_до_цели ** 2 /(2 * эквивалентный_радиус_Земли) + высота_позиции_РЛС_над_уровнем_моря + высота_фазового_центра_антенны
    '''
)


class HeightAim(SimplePythonDataflowBlock):
             
    наклонная_дальность_до_цели = UserPortIn()
    угол_места_цели = UserPortIn()      
    эквивалентный_радиус_Земли = UserPortIn()
    высота_позиции_РЛС_над_уровнем_моря = UserPortIn()    
    высота_фазового_центра_антенны = UserPortIn()  

    высота_цели = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_HEIGHT_AIM):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 32 (35)
DEFAULT_CALC_SOURCE_DISPERSION_HEIGHT = dedent(
    '''
    import numpy as np

    дисперсия_оценки_высоты = ( np.sin(угол_места_цели) + наклонная_дальность_до_цели/эквивалентный_радиус_Земли) ** 2 * СКО_измерения_дальности ** 2 + (наклонная_дальность_до_цели * np.cos(угол_места_цели)) ** 2 * СКО_угловой_координаты_по_углу_места ** 2
    '''
)


class DispersionHeight(SimplePythonDataflowBlock):
             
    угол_места_цели = UserPortIn()
    наклонная_дальность_до_цели = UserPortIn()      
    эквивалентный_радиус_Земли = UserPortIn()
    СКО_измерения_дальности = UserPortIn()    
    наклонная_дальность_до_цели = UserPortIn()  
    СКО_угловой_координаты_по_углу_места = UserPortIn() 

    дисперсия_оценки_высоты = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DISPERSION_HEIGHT):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#33 (36)
DEFAULT_CALC_SOURCE_DISPERSION_X = dedent(
    '''
    import numpy as np
    
    дисперсия_оценки_прямоугольной_координаты_х = (СКО_измерения_дальности * np.cos(угол_места_цели) * np.cos(азимут_места_цели)) ** 2 + ( СКО_угловой_координаты_по_азимуту * наклонная_дальность_до_цели * np.cos(угол_места_цели) * np.sin(азимут_места_цели) ) ** 2 + (СКО_угловой_координаты_по_углу_места * наклонная_дальность_до_цели * np.sin(угол_места_цели) * np.cos(азимут_места_цели)) ** 2
    '''
)


class DispersionX(SimplePythonDataflowBlock):
             
    СКО_измерения_дальности = UserPortIn()
    угол_места_цели = UserPortIn()      
    азимут_места_цели = UserPortIn()
    СКО_угловой_координаты_по_азимуту = UserPortIn()    
    СКО_угловой_координаты_по_углу_места = UserPortIn()  
    наклонная_дальность_до_цели = UserPortIn()    

    дисперсия_оценки_прямоугольной_координаты_х = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DISPERSION_X):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#34 (37)
DEFAULT_CALC_SOURCE_DISPERSION_Y = dedent(
    '''
    import numpy as np

    дисперсия_оценки_прямоугольной_координаты_у = (СКО_измерения_дальности * np.cos(угол_места_цели) * np.sin(азимут_места_цели)) ** 2 + ( СКО_угловой_координаты_по_азимуту * наклонная_дальность_до_цели * np.cos(угол_места_цели) * np.cos(азимут_места_цели) ) ** 2 + (СКО_угловой_координаты_по_углу_места * наклонная_дальность_до_цели * np.sin(угол_места_цели) * np.sin(азимут_места_цели)) ** 2
    '''
)


class DispersionY(SimplePythonDataflowBlock):
             
    СКО_измерения_дальности = UserPortIn()
    угол_места_цели = UserPortIn()      
    азимут_места_цели = UserPortIn()
    СКО_угловой_координаты_по_азимуту = UserPortIn()    
    СКО_угловой_координаты_по_углу_места = UserPortIn()  
    наклонная_дальность_до_цели = UserPortIn()    

    дисперсия_оценки_прямоугольной_координаты_у = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DISPERSION_Y):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#35 (38)
DEFAULT_CALC_SOURCE_DISPERSION_XY = dedent(
    '''
    import numpy as np

    дисперсия_оценки_прямоугольных_координат_ху = (СКО_измерения_дальности ** 2 + (СКО_угловой_координаты_по_азимуту * наклонная_дальность_до_цели) ** 2) * (np.cos(угол_места_цели)) ** 2 + (СКО_угловой_координаты_по_углу_места * наклонная_дальность_до_цели * np.sin(угол_места_цели)) ** 2
    '''
)


class DispersionXY(SimplePythonDataflowBlock):
             
    СКО_измерения_дальности = UserPortIn()
    угол_места_цели = UserPortIn()      
    СКО_угловой_координаты_по_азимуту = UserPortIn()    
    СКО_угловой_координаты_по_углу_места = UserPortIn()  
    наклонная_дальность_до_цели = UserPortIn()    

    дисперсия_оценки_прямоугольных_координат_ху = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DISPERSION_XY):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 38(1) (39)
DEFAULT_CALC_SOURCE_RANGE_RESOLUTION_1 = dedent(
    '''
    import numpy as np
    
    разрешающая_способность_по_дальности = скорость_света *  длительность_импульса / (2 * коэффициент_сжатия_импульса)
    '''
)
class RangeResolution1(SimplePythonDataflowBlock):
             
    длительность_импульса = UserPortIn()
    коэффициент_сжатия_импульса = UserPortIn()        
    скорость_света = UserPortIn()  

    разрешающая_способность_по_дальности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_RANGE_RESOLUTION_1):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 38(2) (40)
DEFAULT_CALC_SOURCE_RANGE_RESOLUTION_2 = dedent(
    '''
    import numpy as np
    
    разрешающая_способность_по_дальности = скорость_света / (2 * ширина_спектра_сигнала )
    '''
)
class RangeResolution2(SimplePythonDataflowBlock):
             
    ширина_спектра_сигнала = UserPortIn()      
    скорость_света = UserPortIn() 

    разрешающая_способность_по_дальности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_RANGE_RESOLUTION_2):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 38(4) (41)
DEFAULT_CALC_SOURCE_RADIAL_VELOCITY_RESOLUTION = dedent(
    '''
    import numpy as np
    
    разрешающая_способность_по_радиальной_скорости = длина_волны * спектр_сигнала / 2
    '''
)
class RadialVelocityResolution(SimplePythonDataflowBlock):
             
    длина_волны = UserPortIn()      
    спектр_сигнала = UserPortIn()  

    разрешающая_способность_по_радиальной_скорости = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_RADIAL_VELOCITY_RESOLUTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 38(5)  (42)
DEFAULT_CALC_SOURCE_HEIGHT_RESOLUTION = dedent(
    '''
    import numpy as np
    
    разрешающая_способность_по_высоте = ширина_ДНА_приемной_антенны * наклонная_дальность_до_цели / np.cos(угол_места_цели)
    '''
)
class HeightResolution(SimplePythonDataflowBlock):
             
    ширина_ДНА_приемной_антенны = UserPortIn()      
    наклонная_дальность_до_цели = UserPortIn()  
    угол_места_цели = UserPortIn() 

    разрешающая_способность_по_высоте = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_HEIGHT_RESOLUTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#42(1) (43)
DEFAULT_CALC_SOURCE_SAMPLING_STEP= dedent(
    '''
    import numpy as np
    
    шаг_дискретизации_времени_задержки_сигнала = 1 / (коэффициент_шага_дискретизации * мгновенная_полоса_сигнала) 
    '''
)
class SamplingStep(SimplePythonDataflowBlock):
             
    коэффициент_шага_дискретизации = UserPortIn()      
    мгновенная_полоса_сигнала = UserPortIn() 

    шаг_дискретизации_времени_задержки_сигнала = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SAMPLING_STEP):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#42(2) 
DEFAULT_CALC_SOURCE_SAMPLING_STEP_2= dedent(
    '''
    import numpy as np
    
    шаг_дискретизации_времени_задержки_сигнала = длительность_зондирующего_импульса / коэффициент_шага_дискретизации  
    '''
)
class SamplingStep2(SimplePythonDataflowBlock):
             
    коэффициент_шага_дискретизации = UserPortIn()      
    длительность_зондирующего_импульса = UserPortIn() 

    шаг_дискретизации_времени_задержки_сигнала = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SAMPLING_STEP_2):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### 45 (44)
DEFAULT_CALC_SOURCE_SIGNAL_EXCEEDANCES = dedent(
    '''
    import numpy as np
    
    мгновенное_значение_превышения_сигнала_над_шумом_по_мощности = среднее_значение_сигнал_шум * значение_функции_случайной_флуктуации_амплитуды_сигнала
    '''
)

class SignalExceedances(SimplePythonDataflowBlock):
             
    среднее_значение_сигнал_шум = UserPortIn()      
    значение_функции_случайной_флуктуации_амплитуды_сигнала = UserPortIn()  

    мгновенное_значение_превышения_сигнала_над_шумом_по_мощности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SIGNAL_EXCEEDANCES):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


#### вместо 52 другая

DEFAULT_CALC_SOURCE_SIGNAL_COEFFICIENT_K = dedent(
    '''
    import numpy as np
    
    коэффициент = 4 * np.pi * расстояние_между_постановщиком_помех_в_направлении_на_подавляемую_РЛС * мощность_передатчика_помех * коэффициент_усиления_антенны_станции_помех_в_направлении_на_подавляемую_РЛС * полоса_пропускания_приемника_РЛС * коэффициент_учитывающий_различие_поляризации_помехи_и_сигнала / (мощность_передатчика_подавляемой_РЛС * коээфициент_антенны_РЛС * ЭПО_самолета_постановщика_помех * ширина_энергетического_спектра_передатчика_помех)
    '''
)

class CoefficientK(SimplePythonDataflowBlock):
             
    расстояние_между_постановщиком_помех_в_направлении_на_подавляемую_РЛС = UserPortIn()      
    мощность_передатчика_помех = UserPortIn()  
    коэффициент_усиления_антенны_станции_помех_в_направлении_на_подавляемую_РЛС = UserPortIn()      
    полоса_пропускания_приемника_РЛС = UserPortIn()  
    коэффициент_учитывающий_различие_поляризации_помехи_и_сигнала = UserPortIn()      
    мощность_передатчика_подавляемой_РЛС = UserPortIn()  
    коээфициент_антенны_РЛС = UserPortIn()      
    ЭПО_самолета_постановщика_помех = UserPortIn()  
    ширина_энергетического_спектра_передатчика_помех = UserPortIn()      

    коэффициент = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SIGNAL_COEFFICIENT_K):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)






##54 (46)
DEFAULT_CALC_SOURCE_MAX_RANGE_NOISE = dedent(
    '''
    import numpy as np
    
    максимальная_дальность_мешающих_отражений_от_земной_поверхности = 4 * высота_фазового_центра_антенны_над_землей * средний_размер_неровностей / длина_волны
    '''
)
class MaxRangeNoise(SimplePythonDataflowBlock):
             
    высота_фазового_центра_антенны_над_землей = UserPortIn()      
    средний_размер_неровностей = UserPortIn()  
    длина_волны = UserPortIn() 

    максимальная_дальность_мешающих_отражений_от_земной_поверхности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_MAX_RANGE_NOISE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 59 (47)
DEFAULT_CALC_SOURCE_SIGNAL_EXCEEDANCES_POWER = dedent(
    '''
    import numpy as np
    
    превышение_сигнала_от_земли_над_шумом_по_мощности = потенциал_РЛС * удельная_ЭПР_энного_участка_земли * ширина_ДНА_по_половинной_мощности_по_азимуту * скорость_света * длительность_импульса / (2 * удаление_энного_участка_земли_от_РЛС ** 3 * np.cos(угол_места))
    '''
)
class SignalExceedancesPower(SimplePythonDataflowBlock):
             
    потенциал_РЛС = UserPortIn()      
    удельная_ЭПР_энного_участка_земли = UserPortIn()  
    ширина_ДНА_по_половинной_мощности_по_азимуту = UserPortIn()      
    скорость_света = UserPortIn()  
    длительность_импульса = UserPortIn()      
    удаление_энного_участка_земли_от_РЛС = UserPortIn()  
    угол_места = UserPortIn() 

    превышение_сигнала_от_земли_над_шумом_по_мощности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SIGNAL_EXCEEDANCES_POWER):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 60 (48)
DEFAULT_CALC_SOURCE_SPECIFIC_RCS = dedent(
    '''
    import numpy as np
    
    удельная_ЭПР = 3.2 * 10 ** (- коэффициент_пропорциональности_для_расчета_удельной_ЭПР_земной_поверхности /  длина_волны)
    '''
)
class SpecificRcs(SimplePythonDataflowBlock):
             
    коэффициент_пропорциональности_для_расчета_удельной_ЭПР_земной_поверхности = UserPortIn()      
    длина_волны = UserPortIn() 

    удельная_ЭПР = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SPECIFIC_RCS):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



#### 61 (49)
DEFAULT_CALC_SOURCE_RCS_SEA = dedent(
    '''
    import numpy as np
    
    удельная_ЭПР_морской_поверхности_для_малых_углов_места = -64 + 6 * баллы_по_шкале_Бофорта + 10 * np.log10(np.sin(угол_места))
    '''
)
class RcsSea(SimplePythonDataflowBlock):
             
    баллы_по_шкале_Бофорта = UserPortIn()      
    угол_места = UserPortIn() 

    удельная_ЭПР_морской_поверхности_для_малых_углов_места = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_RCS_SEA):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

#### 62??? (50)
DEFAULT_CALC_SOURCE_SIGNAL_NOISE_RATIO_WITH_EARTH = dedent(
    '''
    import numpy as np
    
    отношение_сигнал_шум = 16 * np.sin(2 * np.pi * высота_фазового_центра_антенны_над_землей / длина_волны * np.sin(угол_места_цели))** 4 * потенциал_РЛС * ЭПР_цели / (рубеж_обнаружения_цели ** 4)
    '''
)
class SignalNoiseRatioWithEarth(SimplePythonDataflowBlock):
             
    высота_фазового_центра_антенны_над_землей = UserPortIn()      
    длина_волны = UserPortIn() 
    угол_места_цели = UserPortIn()      
    потенциал_РЛС = UserPortIn() 
    ЭПР_цели = UserPortIn()      
    рубеж_обнаружения_цели = UserPortIn() 

    отношение_сигнал_шум = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SIGNAL_NOISE_RATIO_WITH_EARTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)












DEFAULT_CALC_SOURCE_STANDART_DEVIATION_RANGE = dedent(
    '''
    import numpy as np


    СКО_по_дальности = ( разрешающая_способность ) / ( отношение_сигнал_шум**0.5 )
    '''
)


class StandartDeviationRange(SimplePythonDataflowBlock):
    отношение_сигнал_шум = UserPortIn()
    разрешающая_способность = UserPortIn()
    СКО_по_дальности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_STANDART_DEVIATION_RANGE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)




DEFAULT_CALC_SOURCE_STANDART_DEVIATION_ELEVATION = dedent(
    '''
    import numpy as np


    СКО_по_азимуту = ( ширина_ДНА_по_месту ) / ( отношение_сигнал_шум**0.5 )
    '''
)


class StandartDeviationElevation(SimplePythonDataflowBlock):
    отношение_сигнал_шум = UserPortIn()
    ширина_ДНА_по_месту = UserPortIn()
    СКО_по_месту = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_STANDART_DEVIATION_ELEVATION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_STANDART_DEVIATION_AZIMUTH = dedent(
    '''
    import numpy as np


    СКО_по_азимуту = ( ширина_ДНА_по_азимуту ) / ( отношение_сигнал_шум**0.5 )
    '''
)


class StandartDeviationAzimuth(SimplePythonDataflowBlock):
    отношение_сигнал_шум = UserPortIn()
    ширина_ДНА_по_азимуту = UserPortIn()
    СКО_по_азимуту = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_STANDART_DEVIATION_AZIMUTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)




DEFAULT_CALC_SOURCE_RANGE_RESOLUTION = dedent(
    '''
    import numpy as np


    разрешение_по_дальности = ( длительность_импульса * 3e8 ) / 2
    '''
)


class RangeResolution(SimplePythonDataflowBlock):
    длительность_импульса = UserPortIn()
    разрешение_по_дальности = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_RANGE_RESOLUTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)





DEFAULT_CALC_SOURCE_BLINDRANGE = dedent(
    '''
    import numpy as np


    слепая_дальность = ( длительность_импульса + длительность_защитного_интервала ) * 3e8 / 2
    '''
)


class BlindRange(SimplePythonDataflowBlock):
    дительность_импульса = UserPortIn()
    длительность_защитного_интервала = UserPortIn()
    слепая_дальность = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_BLINDRANGE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)




DEFAULT_CALC_SOURCE_BANDWIDTH = dedent(
    '''
    import numpy as np


    ширина_полосы_приемника = ширина_спектра_сигнала + 2 * ( 5000 * несущая_частота ) / ( 3e8)
    '''
)


class BandWidth(SimplePythonDataflowBlock):
    ширина_спектра_сигнала = UserPortIn()
    несущая_частота = UserPortIn()
    ширина_полосы_приемника = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_BANDWIDTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)




DEFAULT_CALC_SOURCE_FREQPULSE = dedent(
    '''
    import numpy as np


    частота_повторения_импульсов = 1 / период_повторения
    '''
)


class FreqPulse(SimplePythonDataflowBlock):
    период_повторения = UserPortIn()
    частота_повторения_импульсов = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_FREQPULSE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

DEFAULT_CALC_SOURCE_DUTY_CYCLE = dedent(
    '''
    import numpy as np


    скважность = период_повторения / длительность_импульса
    '''
)


class DutyCycle(SimplePythonDataflowBlock):
    период_повторения = UserPortIn()
    длительность_импульса = UserPortIn()
    скважность = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DUTY_CYCLE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_TIME_SAVE= dedent(
    '''
    import numpy as np


    скважность = период_повторения * количество_накапливаемых_импульсов
    '''
)


class TimeOfSave(SimplePythonDataflowBlock):
    период_повторения = UserPortIn()
    количество_накапливаемых_импульсов = UserPortIn()
    время_накопления_импульсов = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_TIME_SAVE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_MEAN_POWER_ANTENNA = dedent(
    '''
    import numpy as np


    средняя_мощность_излучения = длительность_импульса / период_повторения * импульсная_мощность
    '''
)


class MeanPowerA(SimplePythonDataflowBlock):
    длительность_импульса = UserPortIn()
    период_повторения = UserPortIn()
    импульсная_мощность = UserPortIn()
    средняя_мощность_излучения = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_MEAN_POWER_ANTENNA):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_WAVELENGTH= dedent(
    '''
    import numpy as np


    длина_волны = 3 * 10**8 / частота
    '''
)


class WaveLength(SimplePythonDataflowBlock):
    частота = UserPortIn()
    длина_волны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_WAVELENGTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_ANTENNA_HIGHT = dedent(
    '''
    import numpy as np


    высота_антенного_полотна = 0.5 * длина_волны * количество_излучателей_место
    '''
)


class AntennaHight(SimplePythonDataflowBlock):
    количество_излучателей_место = UserPortIn()
    длина_волны = UserPortIn()
    высота_антенного_полотна = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_HIGHT):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

DEFAULT_CALC_SOURCE_ANTENNA_HIGH = dedent(
    '''
    import numpy as np


    высота_антенного_полотна = 0.5 * длина_волны * количество_излучателей_место
    '''
)


class AntennaHigh(SimplePythonDataflowBlock):
    количество_излучателей_место = UserPortIn()
    длина_волны = UserPortIn()
    высота_антенного_полотна = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_HIGH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

DEFAULT_CALC_SOURCE_ANTENNA_WIDTH = dedent(
    '''
    import numpy as np


    ширина_антенного_полотна = 0.5 * длина_волны * количество_излучателей_азимут
    '''
)


class AntennaWidth(SimplePythonDataflowBlock):
    количество_излучателей_азимут = UserPortIn()
    длина_волны = UserPortIn()
    ширина_антенного_полотна = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_WIDTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_DNA_AZIMUTH = dedent(
    '''
    import numpy as np


    ширина_ДНА_азимут = 60 * длина_волны / ( ширина_антенны )
    '''
)


class DNAAzimuth(SimplePythonDataflowBlock):
    длина_волны = UserPortIn()
    ширина_антенны = UserPortIn()
    ширина_ДНА_азимут = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DNA_AZIMUTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_DNA_ELEVATION = dedent(
    '''
    import numpy as np


    ширина_ДНА_место = 60 * длина_волны / ( высота_антенны )
    '''
)


class DNAElevation(SimplePythonDataflowBlock):
    длина_волны = UserPortIn()
    высота_антенны = UserPortIn()
    ширина_ДНА_место = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_DNA_ELEVATION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

DEFAULT_CALC_SOURCE_ANTENNA_GAIN = dedent(
    '''
    import numpy as np


    КУ_антенны = 4 * np.pi * 0.6 *  ширина_антенны * высота_антенны / ( длина_волны**2 )
    '''
)


class AntennaGain(SimplePythonDataflowBlock):
    длина_волны = UserPortIn()
    высота_антенны = UserPortIn()
    ширина_антенны = UserPortIn()
    КУ_антенны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_GAIN):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_IMPULSE_POWER = dedent(
    '''
    import numpy as np


    импульсная_мощность = средняя_мощность_передатчика * скважность
    '''
)


class ImpulsePower(SimplePythonDataflowBlock):
    средняя_мощность_передатчика = UserPortIn()
    скважность = UserPortIn()
    импульсная_мощность = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_IMPULSE_POWER):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_SNR = dedent(
    '''
    import numpy as np


    отношение_сигнал_шум = np.power(10, 0.1 * отношение_сигнал_шум_в_дБ)
    '''
)


class SNR(SimplePythonDataflowBlock):
    отношение_сигнал_шум_в_дБ = UserPortIn()
    отношение_сигнал_шум = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_SNR):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_NOISE = dedent(
    '''
    import numpy as np


    фактор_шума = np.power(10, 0.1 * фактор_шума_в_дБ)
    '''
)


class NoiseFactor(SimplePythonDataflowBlock):
    фактор_шума_в_дБ = UserPortIn()
    фактор_шума = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_NOISE):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_LOSS_HF = dedent(
    '''
    import numpy as np


    потери_в_ВЧ_тракте = np.power(10, 0.1 * потери_в_ВЧ_тракте_в_дБ)
    '''
)


class LossHF(SimplePythonDataflowBlock):
    потери_в_ВЧ_тракте_в_дБ = UserPortIn()
    потери_в_ВЧ_тракте = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_LOSS_HF):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_NOISE_POWER = dedent(
    '''
    import numpy as np


    односторонняя_спектральная_плотность_мощности_шума = постоянная_Больцмана * шумовая_температура_приемника
    '''
)


class NoisePower(SimplePythonDataflowBlock):
    постоянная_Больцмана = UserPortIn()
    шумовая_температура_приемника = UserPortIn()
    односторонняя_спектральная_плотность_мощности_шума = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_NOISE_POWER):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_ELEVATION_SECTOR = dedent(
    '''
    import numpy as np


    сектор_обзора_по_углу_места = np.arctan2(верхняя_граница_зоны_обзора, дальность_верхней_границы_зоны_обзора)
    '''
)


class ElevationSector(SimplePythonDataflowBlock):
    дальность_верхней_границы_зоны_обзора = UserPortIn()
    верхняя_граница_зоны_обзора = UserPortIn()
    сектор_обзора_по_углу_места = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ELEVATION_SECTOR):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_ELEVATION_RESOLUTION = dedent(
    '''
    import numpy as np


    угловое_разрешение_по_углу_места = np.arctan2(разерешение_по_высоте_по_ТЗ, максимальная_дальность_обзора_по_ТЗ)
    '''
)


class ElevationResolution(SimplePythonDataflowBlock):
    разерешение_по_высоте_по_ТЗ = UserPortIn()
    максимальная_дальность_обзора_по_ТЗ = UserPortIn()
    угловое_разрешение_по_углу_места = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ELEVATION_RESOLUTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_ELEVATION_NUM_SECTORS = dedent(
    '''
    import numpy as np


    количество_УМП = np.round(сектор_обзора_по_углу_места / угловое_разрешение_по_углу_места)
    '''
)


class ElevationNumSectors(SimplePythonDataflowBlock):
    сектор_обзора_по_углу_места = UserPortIn()
    угловое_разрешение_по_углу_места = UserPortIn()
    количество_УМП = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ELEVATION_NUM_SECTORS):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_AZIMUTH_RESOLUTION = dedent(
    '''
    import numpy as np


    угловое_разрешение_по_азимуту = np.arcsin(разрешение_по_азимуту_в_км_по_ТЗ / максимальная_дальность_обзора_по_ТЗ)
    '''
)


class AzimuthResolution(SimplePythonDataflowBlock):
    разрешение_по_азимуту_в_км_по_ТЗ = UserPortIn()
    максимальная_дальность_обзора_по_ТЗ = UserPortIn()
    угловое_разрешение_по_азимуту = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_AZIMUTH_RESOLUTION):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_AZIMUTH_NUM_SECTORS = dedent(
    '''
    import numpy as np


    количество_азимутальных_позиций = np.round(разрешение_по_азимуту_в_км_по_ТЗ / угловое_разрешение_по_азимуту)
    '''
)


class AzimuthNumSectors(SimplePythonDataflowBlock):
    разрешение_по_азимуту_в_км_по_ТЗ = UserPortIn()
    угловое_разрешение_по_азимуту = UserPortIn()
    количество_азимутальных_позиций = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_AZIMUTH_NUM_SECTORS):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)





DEFAULT_CALC_SOURCE_ANTENNA_GAIN = dedent(
    '''
    import numpy as np


    КУ_антенны = 4 * np.pi * коэффициент_использования_поверхности *\
        ширина_антенного_полотна * высота_антенного_полотна / np.power(длина_волны ,2)
    '''
)


class AntennaGain(SimplePythonDataflowBlock):
    длина_волны = UserPortIn()
    коэффициент_использования_поверхности = UserPortIn()
    ширина_антенного_полотна = UserPortIn()
    высота_антенного_полотна = UserPortIn()
    КУ_антенны = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ANTENNA_GAIN):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)




#############################################################################
#############################################################################


DEFAULT_CALC_SOURCE_ELEVATION_ANGLES = dedent(
    '''
    import numpy as np


    угол_УМП = угловое_разрешение_по_углу_места * np.arange(1, количество_УМП + 1)
    '''
)


class ElevationAngles(SimplePythonDataflowBlock):
    количество_УМП = UserPortIn()
    угловое_разрешение_по_углу_места = UserPortIn()
    угол_УМП = UserPortOut(type=np.ndarray)

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_ELEVATION_ANGLES):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_MEAN_POWER = dedent(
    '''
    import numpy as np

    угол_УМП = np.asarray(угол_УМП)
    
    средняя_мощность_передатчика =  максимальная_дальность_обзора_по_ТЗ * \
        (4 * np.pi) ** 3 * ( отношение_сигнал_шум ) *\
        ( фактор_шума ) * ( потери_в_ВЧ_тракте ) *\
        ( односторонняя_спектральная_плотность_мощности_шума ) *\
        (np.sum(np.min(((верхняя_граница_зоны_обзора / np.arcsin(угол_УМП)), len(угол_УМП) * [максимальная_дальность_обзора_по_ТЗ]), axis=0))) ** 4 /\
        ((длина_волны * КУ_антенны) ** 2 * ЭПР_цели_по_ТЗ * время_обзора_по_ТЗ)
    '''
)


class MeanPower(SimplePythonDataflowBlock):
    отношение_сигнал_шум = UserPortIn()
    фактор_шума = UserPortIn()
    потери_в_ВЧ_тракте = UserPortIn()
    односторонняя_спектральная_плотность_мощности_шума = UserPortIn()
    верхняя_граница_зоны_обзора = UserPortIn()
    угол_УМП = UserPortIn()
    максимальная_дальность_обзора_по_ТЗ = UserPortIn()
    длина_волны = UserPortIn()
    ЭПР_цели_по_ТЗ = UserPortIn()
    КУ_антенны = UserPortIn()
    время_обзора_по_ТЗ = UserPortIn()

    средняя_мощность_передатчика = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_MEAN_POWER):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)




DEFAULT_CALC_SOURCE_REPEAT_PERIOD = dedent(
    '''
    import numpy as np
    import scipy.constants

    угол_УМП = np.asarray(угол_УМП)

    период_повторения = 2 / scipy.constants.c * np.min(((верхняя_граница_зоны_обзора / np.arcsin(угол_УМП)), len(угол_УМП) * [максимальная_дальность_обзора_по_ТЗ]), axis=0)
    '''
)


class RepeatPeriod(SimplePythonDataflowBlock):
    угол_УМП = UserPortIn()
    верхняя_граница_зоны_обзора = UserPortIn()
    максимальная_дальность_обзора_по_ТЗ = UserPortIn()

    период_повторения = UserPortOut(type=np.ndarray)

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_REPEAT_PERIOD):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)


DEFAULT_CALC_SOURCE_PULSE_LENGTH = dedent(
    '''
    import numpy as np


    длительность_импульса = период_повторения / скважность
    '''
)


class PulseLength(SimplePythonDataflowBlock):
    период_повторения = UserPortIn()
    скважность = UserPortIn()
    длительность_импульса = UserPortOut(type=np.ndarray)

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_PULSE_LENGTH):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_FULL_TIME = dedent(
    '''
    import numpy as np


    фактическое_время_обзора = количество_азимутальных_позиций * np.sum(количество_накапливаемых_импульсов * период_повторения)
    '''
)


class FullTime(SimplePythonDataflowBlock):
    количество_азимутальных_позиций = UserPortIn()
    количество_накапливаемых_импульсов = UserPortIn()
    период_повторения = UserPortIn()
    фактическое_время_обзора = UserPortOut()

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_FULL_TIME):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)



DEFAULT_CALC_SOURCE_PULSE_COUNT = dedent(
    '''
    import numpy as np
    
    угол_УМП = np.asarray(угол_УМП)
    длительность_импульса = np.asarray(длительность_импульса)

    количество_накапливаемых_импульсов = np.ceil(
        (4 * np.pi) ** 3 * ( отношение_сигнал_шум ) *\
        ( фактор_шума ) * ( потери_в_ВЧ_тракте ) *\
        ( односторонняя_спектральная_плотность_мощности_шума ) *\
        (np.min(((верхняя_граница_зоны_обзора / np.arcsin(угол_УМП)), len(угол_УМП) * [максимальная_дальность_обзора_по_ТЗ]), axis=0)) ** 4 /\
        ((длина_волны * КУ_антенны) ** 2 * ЭПР_цели_по_ТЗ * импульсная_мощность * длительность_импульса)
        
        )
    '''
)


class PulseCount(SimplePythonDataflowBlock):
    отношение_сигнал_шум = UserPortIn()
    фактор_шума = UserPortIn()
    потери_в_ВЧ_тракте = UserPortIn()
    односторонняя_спектральная_плотность_мощности_шума = UserPortIn()
    верхняя_граница_зоны_обзора = UserPortIn()
    максимальная_дальность_обзора_по_ТЗ = UserPortIn()
    угол_УМП = UserPortIn()
    длина_волны = UserPortIn()
    ЭПР_цели_по_ТЗ = UserPortIn()
    КУ_антенны = UserPortIn()
    импульсная_мощность = UserPortIn()
    длительность_импульса = UserPortIn()

    количество_накапливаемых_импульсов = UserPortOut(type=np.ndarray)

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_PULSE_COUNT):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)

DEFAULT_CALC_SOURCE_PULSE_COUNT = dedent(
    '''
    import numpy as np
    
    длительность_импульса = np.asarray(длительность_импульса)

    дальность_обнаружения = (
        ( ( КУ_антенны ) * ( КУ_антенны_на_прием ) * ( импульсная_мощность ) * ( количество_накапливаемых_импульсов ) * ( длительность_импульса ) * (длина_волны)**2 * ( ЭПР_цели ) ) /\
        ( (4 * np.pi) ** 3 * ( отношение_сигнал_шум ) *\
        ( фактор_шума ) * ( потери_в_ВЧ_тракте ) *\
        ( односторонняя_спектральная_плотность_мощности_шума ) )      
        ) ** 0.25
    '''
)


class RangeOfDetection(SimplePythonDataflowBlock):
    отношение_сигнал_шум = UserPortIn()
    фактор_шума = UserPortIn()
    потери_в_ВЧ_тракте = UserPortIn()
    односторонняя_спектральная_плотность_мощности_шума = UserPortIn()
    длина_волны = UserPortIn()
    ЭПР_цели = UserPortIn()
    КУ_антенны = UserPortIn()
    КУ_антенны_на_прием = UserPortIn()
    импульсная_мощность = UserPortIn()
    длительность_импульса = UserPortIn()
    количество_накапливаемых_импульсов = UserPortIn()

    дальность_обнаружения = UserPortOut(type=np.ndarray)

    def __init__(self, id: Optional[str] = None, *,
                 user_parameters: Optional[Dict[str, UserParameter]] = None,
                 user_properties: Optional[Dict[str, UserProperty]] = None,
                 user_in_ports: Optional[Dict[str, UserPortIn]] = None,
                 user_out_ports: Optional[Dict[str, UserPortOut]] = None,
                 init_source: str = '',
                 calc_source: str = DEFAULT_CALC_SOURCE_PULSE_COUNT):
        super().__init__(id=id,
                         user_parameters=user_parameters,
                         user_properties=user_properties,
                         user_in_ports=user_in_ports,
                         user_out_ports=user_out_ports,
                         init_source=init_source,
                         calc_source=calc_source)
