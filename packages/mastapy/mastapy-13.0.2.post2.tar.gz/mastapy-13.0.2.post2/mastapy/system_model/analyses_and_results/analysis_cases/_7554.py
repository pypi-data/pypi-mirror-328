"""PartCompoundAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartCompoundAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2859,
        _2860,
        _2861,
        _2863,
        _2865,
        _2866,
        _2867,
        _2869,
        _2870,
        _2872,
        _2873,
        _2874,
        _2875,
        _2877,
        _2878,
        _2879,
        _2880,
        _2882,
        _2884,
        _2885,
        _2887,
        _2888,
        _2890,
        _2891,
        _2893,
        _2895,
        _2896,
        _2898,
        _2900,
        _2901,
        _2902,
        _2904,
        _2906,
        _2908,
        _2909,
        _2910,
        _2912,
        _2913,
        _2915,
        _2916,
        _2917,
        _2918,
        _2920,
        _2921,
        _2922,
        _2924,
        _2926,
        _2928,
        _2929,
        _2931,
        _2932,
        _2934,
        _2935,
        _2936,
        _2937,
        _2938,
        _2939,
        _2940,
        _2942,
        _2944,
        _2945,
        _2946,
        _2947,
        _2948,
        _2949,
        _2951,
        _2952,
        _2954,
        _2955,
        _2957,
        _2959,
        _2960,
        _2962,
        _2963,
        _2965,
        _2966,
        _2968,
        _2969,
        _2971,
        _2972,
        _2973,
        _2974,
        _2975,
        _2976,
        _2977,
        _2978,
        _2980,
        _2981,
        _2982,
        _2983,
        _2984,
        _2986,
        _2987,
        _2989,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3124,
        _3125,
        _3126,
        _3128,
        _3130,
        _3131,
        _3132,
        _3134,
        _3135,
        _3137,
        _3138,
        _3139,
        _3140,
        _3142,
        _3143,
        _3144,
        _3145,
        _3147,
        _3149,
        _3150,
        _3152,
        _3153,
        _3155,
        _3156,
        _3158,
        _3160,
        _3161,
        _3163,
        _3165,
        _3166,
        _3167,
        _3169,
        _3171,
        _3173,
        _3174,
        _3175,
        _3176,
        _3177,
        _3179,
        _3180,
        _3181,
        _3182,
        _3184,
        _3185,
        _3186,
        _3188,
        _3190,
        _3192,
        _3193,
        _3195,
        _3196,
        _3198,
        _3199,
        _3200,
        _3201,
        _3202,
        _3203,
        _3204,
        _3206,
        _3208,
        _3209,
        _3210,
        _3211,
        _3212,
        _3213,
        _3215,
        _3216,
        _3218,
        _3219,
        _3220,
        _3222,
        _3223,
        _3225,
        _3226,
        _3228,
        _3229,
        _3231,
        _3232,
        _3234,
        _3235,
        _3236,
        _3237,
        _3238,
        _3239,
        _3240,
        _3241,
        _3243,
        _3244,
        _3245,
        _3246,
        _3247,
        _3249,
        _3250,
        _3252,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3383,
        _3384,
        _3385,
        _3387,
        _3389,
        _3390,
        _3391,
        _3393,
        _3394,
        _3396,
        _3397,
        _3398,
        _3399,
        _3401,
        _3402,
        _3403,
        _3404,
        _3406,
        _3408,
        _3409,
        _3411,
        _3412,
        _3414,
        _3415,
        _3417,
        _3419,
        _3420,
        _3422,
        _3424,
        _3425,
        _3426,
        _3428,
        _3430,
        _3432,
        _3433,
        _3434,
        _3435,
        _3436,
        _3438,
        _3439,
        _3440,
        _3441,
        _3443,
        _3444,
        _3445,
        _3447,
        _3449,
        _3451,
        _3452,
        _3454,
        _3455,
        _3457,
        _3458,
        _3459,
        _3460,
        _3461,
        _3462,
        _3463,
        _3465,
        _3467,
        _3468,
        _3469,
        _3470,
        _3471,
        _3472,
        _3474,
        _3475,
        _3477,
        _3478,
        _3479,
        _3481,
        _3482,
        _3484,
        _3485,
        _3487,
        _3488,
        _3490,
        _3491,
        _3493,
        _3494,
        _3495,
        _3496,
        _3497,
        _3498,
        _3499,
        _3500,
        _3502,
        _3503,
        _3504,
        _3505,
        _3506,
        _3508,
        _3509,
        _3511,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3642,
        _3643,
        _3644,
        _3646,
        _3648,
        _3649,
        _3650,
        _3652,
        _3653,
        _3655,
        _3656,
        _3657,
        _3658,
        _3660,
        _3661,
        _3662,
        _3663,
        _3665,
        _3667,
        _3668,
        _3670,
        _3671,
        _3673,
        _3674,
        _3676,
        _3678,
        _3679,
        _3681,
        _3683,
        _3684,
        _3685,
        _3687,
        _3689,
        _3691,
        _3692,
        _3693,
        _3694,
        _3695,
        _3697,
        _3698,
        _3699,
        _3700,
        _3702,
        _3703,
        _3704,
        _3706,
        _3708,
        _3710,
        _3711,
        _3713,
        _3714,
        _3716,
        _3717,
        _3718,
        _3719,
        _3720,
        _3721,
        _3722,
        _3724,
        _3726,
        _3727,
        _3728,
        _3729,
        _3730,
        _3731,
        _3733,
        _3734,
        _3736,
        _3737,
        _3738,
        _3740,
        _3741,
        _3743,
        _3744,
        _3746,
        _3747,
        _3749,
        _3750,
        _3752,
        _3753,
        _3754,
        _3755,
        _3756,
        _3757,
        _3758,
        _3759,
        _3761,
        _3762,
        _3763,
        _3764,
        _3765,
        _3767,
        _3768,
        _3770,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3905,
        _3906,
        _3907,
        _3909,
        _3911,
        _3912,
        _3913,
        _3915,
        _3916,
        _3918,
        _3919,
        _3920,
        _3921,
        _3923,
        _3924,
        _3925,
        _3926,
        _3928,
        _3930,
        _3931,
        _3933,
        _3934,
        _3936,
        _3937,
        _3939,
        _3941,
        _3942,
        _3944,
        _3946,
        _3947,
        _3948,
        _3950,
        _3952,
        _3954,
        _3955,
        _3956,
        _3957,
        _3958,
        _3960,
        _3961,
        _3962,
        _3963,
        _3965,
        _3966,
        _3967,
        _3969,
        _3971,
        _3973,
        _3974,
        _3976,
        _3977,
        _3979,
        _3980,
        _3981,
        _3982,
        _3983,
        _3984,
        _3985,
        _3987,
        _3989,
        _3990,
        _3991,
        _3992,
        _3993,
        _3994,
        _3996,
        _3997,
        _3999,
        _4000,
        _4001,
        _4003,
        _4004,
        _4006,
        _4007,
        _4009,
        _4010,
        _4012,
        _4013,
        _4015,
        _4016,
        _4017,
        _4018,
        _4019,
        _4020,
        _4021,
        _4022,
        _4024,
        _4025,
        _4026,
        _4027,
        _4028,
        _4030,
        _4031,
        _4033,
    )
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4175,
        _4176,
        _4177,
        _4179,
        _4181,
        _4182,
        _4183,
        _4185,
        _4186,
        _4188,
        _4189,
        _4190,
        _4191,
        _4193,
        _4194,
        _4195,
        _4196,
        _4198,
        _4200,
        _4201,
        _4203,
        _4204,
        _4206,
        _4207,
        _4209,
        _4211,
        _4212,
        _4214,
        _4216,
        _4217,
        _4218,
        _4220,
        _4222,
        _4224,
        _4225,
        _4226,
        _4227,
        _4228,
        _4230,
        _4231,
        _4232,
        _4233,
        _4235,
        _4236,
        _4237,
        _4239,
        _4241,
        _4243,
        _4244,
        _4246,
        _4247,
        _4249,
        _4250,
        _4251,
        _4252,
        _4253,
        _4254,
        _4255,
        _4257,
        _4259,
        _4260,
        _4261,
        _4262,
        _4263,
        _4264,
        _4266,
        _4267,
        _4269,
        _4270,
        _4271,
        _4273,
        _4274,
        _4276,
        _4277,
        _4279,
        _4280,
        _4282,
        _4283,
        _4285,
        _4286,
        _4287,
        _4288,
        _4289,
        _4290,
        _4291,
        _4292,
        _4294,
        _4295,
        _4296,
        _4297,
        _4298,
        _4300,
        _4301,
        _4303,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4451,
        _4452,
        _4453,
        _4455,
        _4457,
        _4458,
        _4459,
        _4461,
        _4462,
        _4464,
        _4465,
        _4466,
        _4467,
        _4469,
        _4470,
        _4471,
        _4472,
        _4474,
        _4476,
        _4477,
        _4479,
        _4480,
        _4482,
        _4483,
        _4485,
        _4487,
        _4488,
        _4490,
        _4492,
        _4493,
        _4494,
        _4496,
        _4498,
        _4500,
        _4501,
        _4502,
        _4503,
        _4504,
        _4506,
        _4507,
        _4508,
        _4509,
        _4511,
        _4512,
        _4513,
        _4515,
        _4517,
        _4519,
        _4520,
        _4522,
        _4523,
        _4525,
        _4526,
        _4527,
        _4528,
        _4529,
        _4530,
        _4531,
        _4533,
        _4535,
        _4536,
        _4537,
        _4538,
        _4539,
        _4540,
        _4542,
        _4543,
        _4545,
        _4546,
        _4547,
        _4549,
        _4550,
        _4552,
        _4553,
        _4555,
        _4556,
        _4558,
        _4559,
        _4561,
        _4562,
        _4563,
        _4564,
        _4565,
        _4566,
        _4567,
        _4568,
        _4570,
        _4571,
        _4572,
        _4573,
        _4574,
        _4576,
        _4577,
        _4579,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4736,
        _4737,
        _4738,
        _4740,
        _4742,
        _4743,
        _4744,
        _4746,
        _4747,
        _4749,
        _4750,
        _4751,
        _4752,
        _4754,
        _4755,
        _4756,
        _4757,
        _4759,
        _4761,
        _4762,
        _4764,
        _4765,
        _4767,
        _4768,
        _4770,
        _4772,
        _4773,
        _4775,
        _4777,
        _4778,
        _4779,
        _4781,
        _4783,
        _4785,
        _4786,
        _4787,
        _4788,
        _4789,
        _4791,
        _4792,
        _4793,
        _4794,
        _4796,
        _4797,
        _4798,
        _4800,
        _4802,
        _4804,
        _4805,
        _4807,
        _4808,
        _4810,
        _4811,
        _4812,
        _4813,
        _4814,
        _4815,
        _4816,
        _4818,
        _4820,
        _4821,
        _4822,
        _4823,
        _4824,
        _4825,
        _4827,
        _4828,
        _4830,
        _4831,
        _4832,
        _4834,
        _4835,
        _4837,
        _4838,
        _4840,
        _4841,
        _4843,
        _4844,
        _4846,
        _4847,
        _4848,
        _4849,
        _4850,
        _4851,
        _4852,
        _4853,
        _4855,
        _4856,
        _4857,
        _4858,
        _4859,
        _4861,
        _4862,
        _4864,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4996,
        _4997,
        _4998,
        _5000,
        _5002,
        _5003,
        _5004,
        _5006,
        _5007,
        _5009,
        _5010,
        _5011,
        _5012,
        _5014,
        _5015,
        _5016,
        _5017,
        _5019,
        _5021,
        _5022,
        _5024,
        _5025,
        _5027,
        _5028,
        _5030,
        _5032,
        _5033,
        _5035,
        _5037,
        _5038,
        _5039,
        _5041,
        _5043,
        _5045,
        _5046,
        _5047,
        _5048,
        _5049,
        _5051,
        _5052,
        _5053,
        _5054,
        _5056,
        _5057,
        _5058,
        _5060,
        _5062,
        _5064,
        _5065,
        _5067,
        _5068,
        _5070,
        _5071,
        _5072,
        _5073,
        _5074,
        _5075,
        _5076,
        _5078,
        _5080,
        _5081,
        _5082,
        _5083,
        _5084,
        _5085,
        _5087,
        _5088,
        _5090,
        _5091,
        _5092,
        _5094,
        _5095,
        _5097,
        _5098,
        _5100,
        _5101,
        _5103,
        _5104,
        _5106,
        _5107,
        _5108,
        _5109,
        _5110,
        _5111,
        _5112,
        _5113,
        _5115,
        _5116,
        _5117,
        _5118,
        _5119,
        _5121,
        _5122,
        _5124,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5255,
        _5256,
        _5257,
        _5259,
        _5261,
        _5262,
        _5263,
        _5265,
        _5266,
        _5268,
        _5269,
        _5270,
        _5271,
        _5273,
        _5274,
        _5275,
        _5276,
        _5278,
        _5280,
        _5281,
        _5283,
        _5284,
        _5286,
        _5287,
        _5289,
        _5291,
        _5292,
        _5294,
        _5296,
        _5297,
        _5298,
        _5300,
        _5302,
        _5304,
        _5305,
        _5306,
        _5307,
        _5308,
        _5310,
        _5311,
        _5312,
        _5313,
        _5315,
        _5316,
        _5317,
        _5319,
        _5321,
        _5323,
        _5324,
        _5326,
        _5327,
        _5329,
        _5330,
        _5331,
        _5332,
        _5333,
        _5334,
        _5335,
        _5337,
        _5339,
        _5340,
        _5341,
        _5342,
        _5343,
        _5344,
        _5346,
        _5347,
        _5349,
        _5350,
        _5351,
        _5353,
        _5354,
        _5356,
        _5357,
        _5359,
        _5360,
        _5362,
        _5363,
        _5365,
        _5366,
        _5367,
        _5368,
        _5369,
        _5370,
        _5371,
        _5372,
        _5374,
        _5375,
        _5376,
        _5377,
        _5378,
        _5380,
        _5381,
        _5383,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5537,
        _5538,
        _5539,
        _5541,
        _5543,
        _5544,
        _5545,
        _5547,
        _5548,
        _5550,
        _5551,
        _5552,
        _5553,
        _5555,
        _5556,
        _5557,
        _5558,
        _5560,
        _5562,
        _5563,
        _5565,
        _5566,
        _5568,
        _5569,
        _5571,
        _5573,
        _5574,
        _5576,
        _5578,
        _5579,
        _5580,
        _5582,
        _5584,
        _5586,
        _5587,
        _5588,
        _5589,
        _5590,
        _5592,
        _5593,
        _5594,
        _5595,
        _5597,
        _5598,
        _5599,
        _5601,
        _5603,
        _5605,
        _5606,
        _5608,
        _5609,
        _5611,
        _5612,
        _5613,
        _5614,
        _5615,
        _5616,
        _5617,
        _5619,
        _5621,
        _5622,
        _5623,
        _5624,
        _5625,
        _5626,
        _5628,
        _5629,
        _5631,
        _5632,
        _5633,
        _5635,
        _5636,
        _5638,
        _5639,
        _5641,
        _5642,
        _5644,
        _5645,
        _5647,
        _5648,
        _5649,
        _5650,
        _5651,
        _5652,
        _5653,
        _5654,
        _5656,
        _5657,
        _5658,
        _5659,
        _5660,
        _5662,
        _5663,
        _5665,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5887,
        _5888,
        _5889,
        _5891,
        _5893,
        _5894,
        _5895,
        _5897,
        _5898,
        _5900,
        _5901,
        _5902,
        _5903,
        _5905,
        _5906,
        _5907,
        _5908,
        _5910,
        _5912,
        _5913,
        _5915,
        _5916,
        _5918,
        _5919,
        _5921,
        _5923,
        _5924,
        _5926,
        _5928,
        _5929,
        _5930,
        _5932,
        _5934,
        _5936,
        _5937,
        _5938,
        _5939,
        _5940,
        _5942,
        _5943,
        _5944,
        _5945,
        _5947,
        _5948,
        _5949,
        _5951,
        _5953,
        _5955,
        _5956,
        _5958,
        _5959,
        _5961,
        _5962,
        _5963,
        _5964,
        _5965,
        _5966,
        _5967,
        _5969,
        _5971,
        _5972,
        _5973,
        _5974,
        _5975,
        _5976,
        _5978,
        _5979,
        _5981,
        _5982,
        _5983,
        _5985,
        _5986,
        _5988,
        _5989,
        _5991,
        _5992,
        _5994,
        _5995,
        _5997,
        _5998,
        _5999,
        _6000,
        _6001,
        _6002,
        _6003,
        _6004,
        _6006,
        _6007,
        _6008,
        _6009,
        _6010,
        _6012,
        _6013,
        _6015,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6147,
        _6148,
        _6149,
        _6151,
        _6153,
        _6154,
        _6155,
        _6157,
        _6158,
        _6160,
        _6161,
        _6162,
        _6163,
        _6165,
        _6166,
        _6167,
        _6168,
        _6170,
        _6172,
        _6173,
        _6175,
        _6176,
        _6178,
        _6179,
        _6181,
        _6183,
        _6184,
        _6186,
        _6188,
        _6189,
        _6190,
        _6192,
        _6194,
        _6196,
        _6197,
        _6198,
        _6199,
        _6200,
        _6202,
        _6203,
        _6204,
        _6205,
        _6207,
        _6208,
        _6209,
        _6211,
        _6213,
        _6215,
        _6216,
        _6218,
        _6219,
        _6221,
        _6222,
        _6223,
        _6224,
        _6225,
        _6226,
        _6227,
        _6229,
        _6231,
        _6232,
        _6233,
        _6234,
        _6235,
        _6236,
        _6238,
        _6239,
        _6241,
        _6242,
        _6243,
        _6245,
        _6246,
        _6248,
        _6249,
        _6251,
        _6252,
        _6254,
        _6255,
        _6257,
        _6258,
        _6259,
        _6260,
        _6261,
        _6262,
        _6263,
        _6264,
        _6266,
        _6267,
        _6268,
        _6269,
        _6270,
        _6272,
        _6273,
        _6275,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6416,
        _6417,
        _6418,
        _6420,
        _6422,
        _6423,
        _6424,
        _6426,
        _6427,
        _6429,
        _6430,
        _6431,
        _6432,
        _6434,
        _6435,
        _6436,
        _6437,
        _6439,
        _6441,
        _6442,
        _6444,
        _6445,
        _6447,
        _6448,
        _6450,
        _6452,
        _6453,
        _6455,
        _6457,
        _6458,
        _6459,
        _6461,
        _6463,
        _6465,
        _6466,
        _6467,
        _6468,
        _6469,
        _6471,
        _6472,
        _6473,
        _6474,
        _6476,
        _6477,
        _6478,
        _6480,
        _6482,
        _6484,
        _6485,
        _6487,
        _6488,
        _6490,
        _6491,
        _6492,
        _6493,
        _6494,
        _6495,
        _6496,
        _6498,
        _6500,
        _6501,
        _6502,
        _6503,
        _6504,
        _6505,
        _6507,
        _6508,
        _6510,
        _6511,
        _6512,
        _6514,
        _6515,
        _6517,
        _6518,
        _6520,
        _6521,
        _6523,
        _6524,
        _6526,
        _6527,
        _6528,
        _6529,
        _6530,
        _6531,
        _6532,
        _6533,
        _6535,
        _6536,
        _6537,
        _6538,
        _6539,
        _6541,
        _6542,
        _6544,
    )
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6683,
        _6684,
        _6685,
        _6687,
        _6689,
        _6690,
        _6691,
        _6693,
        _6694,
        _6696,
        _6697,
        _6698,
        _6699,
        _6701,
        _6702,
        _6703,
        _6704,
        _6706,
        _6708,
        _6709,
        _6711,
        _6712,
        _6714,
        _6715,
        _6717,
        _6719,
        _6720,
        _6722,
        _6724,
        _6725,
        _6726,
        _6728,
        _6730,
        _6732,
        _6733,
        _6734,
        _6735,
        _6736,
        _6738,
        _6739,
        _6740,
        _6741,
        _6743,
        _6744,
        _6745,
        _6747,
        _6749,
        _6751,
        _6752,
        _6754,
        _6755,
        _6757,
        _6758,
        _6759,
        _6760,
        _6761,
        _6762,
        _6763,
        _6765,
        _6767,
        _6768,
        _6769,
        _6770,
        _6771,
        _6772,
        _6774,
        _6775,
        _6777,
        _6778,
        _6779,
        _6781,
        _6782,
        _6784,
        _6785,
        _6787,
        _6788,
        _6790,
        _6791,
        _6793,
        _6794,
        _6795,
        _6796,
        _6797,
        _6798,
        _6799,
        _6800,
        _6802,
        _6803,
        _6804,
        _6805,
        _6806,
        _6808,
        _6809,
        _6811,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7149,
        _7150,
        _7151,
        _7153,
        _7155,
        _7156,
        _7157,
        _7159,
        _7160,
        _7162,
        _7163,
        _7164,
        _7165,
        _7167,
        _7168,
        _7169,
        _7170,
        _7172,
        _7174,
        _7175,
        _7177,
        _7178,
        _7180,
        _7181,
        _7183,
        _7185,
        _7186,
        _7188,
        _7190,
        _7191,
        _7192,
        _7194,
        _7196,
        _7198,
        _7199,
        _7200,
        _7201,
        _7202,
        _7204,
        _7205,
        _7206,
        _7207,
        _7209,
        _7210,
        _7211,
        _7213,
        _7215,
        _7217,
        _7218,
        _7220,
        _7221,
        _7223,
        _7224,
        _7225,
        _7226,
        _7227,
        _7228,
        _7229,
        _7231,
        _7233,
        _7234,
        _7235,
        _7236,
        _7237,
        _7238,
        _7240,
        _7241,
        _7243,
        _7244,
        _7245,
        _7247,
        _7248,
        _7250,
        _7251,
        _7253,
        _7254,
        _7256,
        _7257,
        _7259,
        _7260,
        _7261,
        _7262,
        _7263,
        _7264,
        _7265,
        _7266,
        _7268,
        _7269,
        _7270,
        _7271,
        _7272,
        _7274,
        _7275,
        _7277,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7414,
        _7415,
        _7416,
        _7418,
        _7420,
        _7421,
        _7422,
        _7424,
        _7425,
        _7427,
        _7428,
        _7429,
        _7430,
        _7432,
        _7433,
        _7434,
        _7435,
        _7437,
        _7439,
        _7440,
        _7442,
        _7443,
        _7445,
        _7446,
        _7448,
        _7450,
        _7451,
        _7453,
        _7455,
        _7456,
        _7457,
        _7459,
        _7461,
        _7463,
        _7464,
        _7465,
        _7466,
        _7467,
        _7469,
        _7470,
        _7471,
        _7472,
        _7474,
        _7475,
        _7476,
        _7478,
        _7480,
        _7482,
        _7483,
        _7485,
        _7486,
        _7488,
        _7489,
        _7490,
        _7491,
        _7492,
        _7493,
        _7494,
        _7496,
        _7498,
        _7499,
        _7500,
        _7501,
        _7502,
        _7503,
        _7505,
        _7506,
        _7508,
        _7509,
        _7510,
        _7512,
        _7513,
        _7515,
        _7516,
        _7518,
        _7519,
        _7521,
        _7522,
        _7524,
        _7525,
        _7526,
        _7527,
        _7528,
        _7529,
        _7530,
        _7531,
        _7533,
        _7534,
        _7535,
        _7536,
        _7537,
        _7539,
        _7540,
        _7542,
    )
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAnalysis",)


Self = TypeVar("Self", bound="PartCompoundAnalysis")


class PartCompoundAnalysis(_7551.DesignEntityCompoundAnalysis):
    """PartCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundAnalysis")

    class _Cast_PartCompoundAnalysis:
        """Special nested class for casting PartCompoundAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
            parent: "PartCompoundAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2860.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(_2860.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2861.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2865.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(
                _2865.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2866.AssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2867.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BearingCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2869.BeltDriveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2870.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(
                _2870.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2872.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(
                _2872.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2873.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(
                _2873.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2874.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(
                _2874.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2877.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2878.BoltCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2879.BoltedJointCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2880.ClutchCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ClutchCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2882.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ClutchHalfCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2885.ConceptCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2887.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2888.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2890.ConceptGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2893.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.ConicalGearSetCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2895.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2896.CouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CouplingCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2898.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2900.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2901.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2902.CycloidalAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2904.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2906.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2908.CylindricalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2909.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(
                _2909.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2910.DatumCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2912.ExternalCADModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2913.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2915.FaceGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2916.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2917.FlexiblePinAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(_2917.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2920.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2921.GuideDxfModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(_2921.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2922.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(_2922.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2924.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(_2924.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2928.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(
                _2928.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2931.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(
                _2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2934.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(
                _2934.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2935.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2936.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(
                _2936.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2938.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.OilSealCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2940.PartToPartShearCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2942.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2944.PlanetaryGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2945.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(_2945.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2946.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2947.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(_2947.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2948.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2949.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2951.RollingRingAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2952.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.RollingRingCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2954.RootAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2955.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(_2955.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2957.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(_2957.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2960.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2962.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2963.SpringDamperCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2965.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2966.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2968.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(
                _2968.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2969.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2971.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2972.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(
                _2972.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2973.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(
                _2973.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2974.SynchroniserCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2975.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2976.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2977.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2978.TorqueConverterCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2980.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2981.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(
                _2981.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2982.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2983.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(_2983.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2984.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2984,
            )

            return self._parent._cast(_2984.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2986.WormGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(_2986.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2987.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(_2987.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2989.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3125.AbstractShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3125,
            )

            return self._parent._cast(
                _3125.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3126.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3128.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3130,
            )

            return self._parent._cast(
                _3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3131.AssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3132.BearingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3132,
            )

            return self._parent._cast(
                _3132.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3134.BeltDriveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3134,
            )

            return self._parent._cast(
                _3134.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3135.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3135,
            )

            return self._parent._cast(
                _3135.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3137.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3138.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3139.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3140.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3142.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolt_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3143.BoltCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(_3143.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3144.BoltedJointCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3145.ClutchCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3147.ClutchHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3149.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3150.ConceptCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3152.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3153.ConceptGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3155.ConceptGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3156.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3158.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3160.ConnectorCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3161.CouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3163.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3165.CVTCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(_3165.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3166.CVTPulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3166,
            )

            return self._parent._cast(
                _3166.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3167.CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(
                _3167.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3169.CycloidalDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3171.CylindricalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3173.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3174.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def datum_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3175.DatumCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(_3175.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3176.ExternalCADModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.ExternalCADModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3177.FaceGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3179.FaceGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3180.FEPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(
                _3180.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3181.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3182.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(_3182.GearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3184.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3185.GuideDxfModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3185,
            )

            return self._parent._cast(
                _3185.GuideDxfModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3186.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3188.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3188,
            )

            return self._parent._cast(
                _3188.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3190.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3192.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3193.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3195.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3196.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3198.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3199.MassDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3200.MeasurementComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3201.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3202.OilSealCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3204.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3206.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3206,
            )

            return self._parent._cast(
                _3206.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3208.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3209.PlanetCarrierCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3210.PointLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3210,
            )

            return self._parent._cast(
                _3210.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3211.PowerLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3212.PulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3213.RingPinsCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(
                _3213.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3215.RollingRingAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3216.RollingRingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3218.RootAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(
                _3218.RootAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3219.ShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(_3219.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3220.ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3223.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3225.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3226.SpringDamperCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3228.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3229.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3231.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3232.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3234.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3235.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3236.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3237.SynchroniserCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3238.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3239.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3240.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3241.TorqueConverterCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3243.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3244.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3245.UnbalancedMassCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3246.VirtualComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3247.WormGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3247,
            )

            return self._parent._cast(
                _3247.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3249.WormGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3249,
            )

            return self._parent._cast(
                _3249.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3250.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3250,
            )

            return self._parent._cast(
                _3250.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3252.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3252,
            )

            return self._parent._cast(
                _3252.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3383.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3383,
            )

            return self._parent._cast(
                _3383.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3384,
            )

            return self._parent._cast(
                _3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3385.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3387.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3389.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3389,
            )

            return self._parent._cast(
                _3389.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3390.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3390,
            )

            return self._parent._cast(
                _3390.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3391.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3391,
            )

            return self._parent._cast(
                _3391.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3393.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3393,
            )

            return self._parent._cast(
                _3393.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3394,
            )

            return self._parent._cast(
                _3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3396.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3397.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3398.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3401.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3402.BoltCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.BoltCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3403.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3403,
            )

            return self._parent._cast(
                _3403.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3404.ClutchCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3406.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3409.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3411.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3412.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3414.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3415.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3415,
            )

            return self._parent._cast(
                _3415.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3417.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3417,
            )

            return self._parent._cast(
                _3417.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3419.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3420.CouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3420,
            )

            return self._parent._cast(
                _3420.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3422,
            )

            return self._parent._cast(
                _3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3424.CVTCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.CVTCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3425.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3425,
            )

            return self._parent._cast(
                _3425.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3426.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3428.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3432.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3433.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3434.DatumCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.DatumCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3435.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3436.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3438.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3439.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3439,
            )

            return self._parent._cast(
                _3439.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3440.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3441.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3443.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3444.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3444,
            )

            return self._parent._cast(
                _3444.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3445.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3447.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3449.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3451.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3452.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3454.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3455.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3457.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3458.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3459.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3461.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3463.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3465.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3465,
            )

            return self._parent._cast(
                _3465.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3467.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3467,
            )

            return self._parent._cast(
                _3467.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3468.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3468,
            )

            return self._parent._cast(
                _3468.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3469.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3470.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3471.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3472.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3474.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3475.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3477.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3478.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3479.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3481.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3481,
            )

            return self._parent._cast(
                _3481.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3482.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3484.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3485.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3487.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3488.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3490.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3490,
            )

            return self._parent._cast(
                _3490.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3491.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3493.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3494.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3495.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3495,
            )

            return self._parent._cast(
                _3495.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3496.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3497.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3498.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3498,
            )

            return self._parent._cast(
                _3498.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3499.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3500.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3502.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3503.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3504.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3504,
            )

            return self._parent._cast(
                _3504.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3505.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3506.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3506,
            )

            return self._parent._cast(
                _3506.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3508.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3508,
            )

            return self._parent._cast(
                _3508.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3509.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3509,
            )

            return self._parent._cast(
                _3509.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3511.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3511,
            )

            return self._parent._cast(
                _3511.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3643.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3643,
            )

            return self._parent._cast(
                _3643.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3644.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3644,
            )

            return self._parent._cast(
                _3644.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3646.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3646,
            )

            return self._parent._cast(
                _3646.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3648.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3648,
            )

            return self._parent._cast(
                _3648.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3649.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3649,
            )

            return self._parent._cast(
                _3649.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3650.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3650,
            )

            return self._parent._cast(
                _3650.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3652.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3652,
            )

            return self._parent._cast(
                _3652.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3653.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3653,
            )

            return self._parent._cast(
                _3653.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3655.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3655,
            )

            return self._parent._cast(
                _3655.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3656.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3656,
            )

            return self._parent._cast(
                _3656.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3657.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3658.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3658,
            )

            return self._parent._cast(
                _3658.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3660.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3661.BoltCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.BoltCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3662.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3662,
            )

            return self._parent._cast(
                _3662.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3663.ClutchCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3665.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3668.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3670.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3671.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3671,
            )

            return self._parent._cast(
                _3671.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3673.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3673,
            )

            return self._parent._cast(
                _3673.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3674.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3676.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3676,
            )

            return self._parent._cast(
                _3676.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3678.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3679.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3679,
            )

            return self._parent._cast(
                _3679.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3681,
            )

            return self._parent._cast(
                _3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3683.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.CVTCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3684.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3684,
            )

            return self._parent._cast(
                _3684.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3685.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3687.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3687,
            )

            return self._parent._cast(
                _3687.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3689.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3689,
            )

            return self._parent._cast(
                _3689.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3691.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3692.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3693.DatumCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.DatumCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3694.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3695.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3695,
            )

            return self._parent._cast(
                _3695.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3697.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3698.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3698,
            )

            return self._parent._cast(
                _3698.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3699.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3700.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3703.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3703,
            )

            return self._parent._cast(
                _3703.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3704.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3704,
            )

            return self._parent._cast(
                _3704.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3706.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3708.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3708,
            )

            return self._parent._cast(
                _3708.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3710.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3711.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3713.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3714.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3716.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3716,
            )

            return self._parent._cast(
                _3716.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3717.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3718.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3720.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3722.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3724.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3726.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3726,
            )

            return self._parent._cast(
                _3726.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3727.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3727,
            )

            return self._parent._cast(
                _3727.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3728.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3729.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3729,
            )

            return self._parent._cast(
                _3729.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3731.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3733.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3733,
            )

            return self._parent._cast(
                _3733.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3734.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3736.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3737.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3737,
            )

            return self._parent._cast(
                _3737.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3738.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3738,
            )

            return self._parent._cast(
                _3738.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3741.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3743.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3744.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3746.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3747.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3749.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3749,
            )

            return self._parent._cast(
                _3749.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3750.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3750,
            )

            return self._parent._cast(
                _3750.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3752.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3753.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3754.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3754,
            )

            return self._parent._cast(
                _3754.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3755.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3756.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3757.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3757,
            )

            return self._parent._cast(
                _3757.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3758.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3759.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3761.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3762.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3762,
            )

            return self._parent._cast(
                _3762.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3763.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3763,
            )

            return self._parent._cast(
                _3763.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3764.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3765.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3765,
            )

            return self._parent._cast(
                _3765.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3767.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3767,
            )

            return self._parent._cast(
                _3767.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3768.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3768,
            )

            return self._parent._cast(
                _3768.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3770.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3770,
            )

            return self._parent._cast(
                _3770.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3906.AbstractShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(_3906.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3907.AbstractShaftOrHousingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3909.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3911.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(
                _3911.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3912.AssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3913.BearingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3915.BeltDriveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3916.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3916,
            )

            return self._parent._cast(
                _3916.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3918.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(
                _3918.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3919.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(
                _3919.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3920.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(
                _3920.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3921.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(_3921.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3923.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3924.BoltCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3925.BoltedJointCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3926.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3928.ClutchHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3931.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3933.ConceptCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3934.ConceptGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3936.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3937.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3939.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3941.ConnectorCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3942.CouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3944.CouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(_3944.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3946.CVTCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3947.CVTPulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3948.CycloidalAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3950.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3952.CylindricalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3954.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3955.CylindricalPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(
                _3955.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3956.DatumCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3957.ExternalCADModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3958.FaceGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3960.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3961.FEPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(_3961.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3962.FlexiblePinAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3963.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3965.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3966.GuideDxfModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(_3966.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3967.HypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(_3967.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3969.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3971.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(
                _3971.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3973.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(
                _3973.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3974.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(
                _3974.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3976.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3977.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(
                _3977.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3979.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(
                _3979.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3980.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3981.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(
                _3981.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3983.OilSealCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.OilSealCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3985.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3987.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3989.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3990.PlanetCarrierCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(_3990.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3991.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(_3991.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3992.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(_3992.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3993.PulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3994.RingPinsCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(_3994.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3996.RollingRingAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(
                _3996.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3997.RollingRingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3999.RootAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4000.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(_4000.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4001.ShaftHubConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(_4001.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4004.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(_4004.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4006.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(_4006.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4007.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4009.SpringDamperHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4010.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(
                _4010.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4012.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(
                _4012.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4013.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4015.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4016.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4017.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(
                _4017.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4018.SynchroniserCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(_4018.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4019.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4020.SynchroniserPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4021.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4022.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4024.TorqueConverterPumpCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(
                _4024.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4025.TorqueConverterTurbineCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(
                _4025.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4026.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4026,
            )

            return self._parent._cast(_4026.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4027.VirtualComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(_4027.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4028.WormGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4028,
            )

            return self._parent._cast(_4028.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4030.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(_4030.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4031.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4031,
            )

            return self._parent._cast(_4031.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4033.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4033,
            )

            return self._parent._cast(_4033.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4176.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4177.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4179.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4181.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4182.AssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4183.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BearingCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4185.BeltDriveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4186.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4188.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4189.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(
                _4189.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4190.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4191.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4193.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4194.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4195.BoltedJointCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4196.ClutchCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ClutchCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4198.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ClutchHalfCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4201.ConceptCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4203.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4204.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4206.ConceptGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4207.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4209.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.ConicalGearSetCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4211.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4212.CouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CouplingCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4214.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4216.CVTCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4217.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4218.CycloidalAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4220.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4222.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4224.CylindricalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4225.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4226.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4227.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4228.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.FaceGearCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4230.FaceGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4231.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4232.FlexiblePinAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(_4232.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4233.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.GearCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4235.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4236.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(_4236.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4237.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4239.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4241.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4243.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(
                _4243.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(
                _4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4246.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(
                _4246.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(
                _4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4249.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(
                _4249.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4250.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4251.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4253.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.OilSealCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4255.PartToPartShearCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4257.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(
                _4257.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4259.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4260.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(_4260.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4261.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4262.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4263.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4264.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4266.RollingRingAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4267.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.RollingRingCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4269.RootAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4270.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4271.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.ShaftHubConnectionCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4274.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4276.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4277.SpringDamperCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4279.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4280.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4282.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4283.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4285.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4286.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4287.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4288.SynchroniserCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4289.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4290.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4291.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4292.TorqueConverterCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4294.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4295.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4296.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4297.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4298.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.WormGearCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4300.WormGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4301.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4303.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4303,
            )

            return self._parent._cast(_4303.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4451.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4452.AbstractShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(_4452.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4453.AbstractShaftOrHousingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4455.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4458.AssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4459.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4461.BeltDriveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4461,
            )

            return self._parent._cast(_4461.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4462.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(
                _4462.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4464.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(
                _4464.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4465.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(
                _4465.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4466.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(
                _4466.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4467.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4469.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4470.BoltCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4471.BoltedJointCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4472.ClutchCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4474.ClutchHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4477.ConceptCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4479.ConceptCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(
                _4479.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4480.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4482.ConceptGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4483.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(_4483.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4485.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4487.ConnectorCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4488.CouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(_4488.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4490.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4492.CVTCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(_4492.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4493.CVTPulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(_4493.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4494.CycloidalAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(
                _4494.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4496.CycloidalDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4498.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4500.CylindricalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(
                _4500.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4501.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(
                _4501.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4502.DatumCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4503.ExternalCADModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4504.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(_4504.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4506.FaceGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(_4506.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4507.FEPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4508.FlexiblePinAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4509.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(_4509.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4511.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4512.GuideDxfModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(_4512.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4513.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(_4513.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4515.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(_4515.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4522.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4523.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4525.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4526.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4527.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(
                _4527.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4529.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.OilSealCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4531.PartToPartShearCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(
                _4531.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4533.PartToPartShearCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(
                _4533.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4535.PlanetaryGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(_4535.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4536.PlanetCarrierCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(_4536.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4537.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(_4537.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4538.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4539.PulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4540.RingPinsCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(_4540.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4542.RollingRingAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(
                _4542.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4543.RollingRingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4545.RootAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4546.ShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(_4546.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4547.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4549.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4550.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(_4550.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4552.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4553.SpringDamperCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(_4553.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4555.SpringDamperHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(_4555.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4556.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(
                _4556.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4558.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4559.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4561.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4562.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4563.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(
                _4563.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4564.SynchroniserCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4565.SynchroniserHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4566.SynchroniserPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4567.SynchroniserSleeveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4568.TorqueConverterCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4570.TorqueConverterPumpCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4571.TorqueConverterTurbineCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4572.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4572,
            )

            return self._parent._cast(_4572.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4573.VirtualComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(_4573.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4574.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(_4574.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4576.WormGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4576,
            )

            return self._parent._cast(_4576.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4577.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4577,
            )

            return self._parent._cast(_4577.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4579.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4579,
            )

            return self._parent._cast(
                _4579.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4737.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(_4737.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4738.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4740.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4742.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4743.AssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(_4743.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4744.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(_4744.BearingCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4746.BeltDriveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4747.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4749.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(
                _4749.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4750.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(
                _4750.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4751.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(
                _4751.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4752.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4754.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4755.BoltCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4756.BoltedJointCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4757.ClutchCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ClutchCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4759.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ClutchHalfCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4762.ConceptCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4764.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4765.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4767.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4768.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4770.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.ConicalGearSetCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4772.ConnectorCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4773.CouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CouplingCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4775.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4777.CVTCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4778.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4779.CycloidalAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4781.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4783.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4785.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4786.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4787.DatumCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4788.ExternalCADModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4789.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4791.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4792.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4793.FlexiblePinAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(_4793.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4794.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.GearCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4796.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(_4796.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4797.GuideDxfModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(_4797.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4798.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(_4798.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4800.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4805.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(
                _4805.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(
                _4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4808.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(
                _4808.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4811.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4812.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4814.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.OilSealCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4816.PartToPartShearCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4818.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(
                _4818.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4820.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4821.PlanetCarrierCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(_4821.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4822.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4823.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4824.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4825.RingPinsCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4827.RollingRingAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4828.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.RollingRingCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4830.RootAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4831.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4832.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4835.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4837.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4838.SpringDamperCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4840.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4841.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4843.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(
                _4843.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4844.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4846.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4847.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(
                _4847.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4848.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4849.SynchroniserCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4850.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4851.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4852.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4853.TorqueConverterCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4855.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4856.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4857.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4857,
            )

            return self._parent._cast(_4857.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4858.VirtualComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4859.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4859,
            )

            return self._parent._cast(_4859.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4861.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4862.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4862,
            )

            return self._parent._cast(_4862.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4864.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4864,
            )

            return self._parent._cast(_4864.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4997.AbstractShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4998.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(
                _4998.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5000.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5002.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5003.AssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5003,
            )

            return self._parent._cast(_5003.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5004.BearingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(_5004.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5006.BeltDriveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(_5006.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5007.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(
                _5007.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5009.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(
                _5009.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5010.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5011.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(
                _5011.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5012.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5014.BevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5015.BoltCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(_5015.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5016.BoltedJointCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5017.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(_5017.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5019.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(_5019.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5021.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(_5021.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5022.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5024.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5025.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(
                _5025.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5027.ConceptGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5028.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5028,
            )

            return self._parent._cast(
                _5028.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5030.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(
                _5030.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5032.ConnectorCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5033.CouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(_5033.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5035.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5037.CVTCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(_5037.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5038.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(_5038.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5039.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5041.CycloidalDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5043.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5045.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5046.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(
                _5046.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def datum_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5047.DatumCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5048.ExternalCADModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(
                _5048.ExternalCADModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5049.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5049,
            )

            return self._parent._cast(_5049.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5051.FaceGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5052.FEPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(_5052.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5053.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5054.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(_5054.GearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5056.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(_5056.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5057.GuideDxfModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.GuideDxfModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5058.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(_5058.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5060.HypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5060,
            )

            return self._parent._cast(
                _5060.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5062.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5064.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5065.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5067.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(
                _5067.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5068.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(
                _5068.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5070.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5071.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(_5071.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5072.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5073.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5074.OilSealCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(_5074.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5076.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(
                _5076.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5078.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5080.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5081.PlanetCarrierCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5082.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(_5082.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5083.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(_5083.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5084.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(_5084.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5085.RingPinsCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(_5085.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5087.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(
                _5087.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5088.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5090.RootAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.RootAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5091.ShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(_5091.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5092.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5095.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5097.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5098.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5100.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5101.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5103.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5104.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5106.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5107.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5108.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5109.SynchroniserCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5110.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5111.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5112.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5113.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5115.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5116.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5117.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5117,
            )

            return self._parent._cast(
                _5117.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5118.VirtualComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5118,
            )

            return self._parent._cast(
                _5118.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5119.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5119,
            )

            return self._parent._cast(_5119.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5121.WormGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5121,
            )

            return self._parent._cast(
                _5121.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5122.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5122,
            )

            return self._parent._cast(
                _5122.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5124.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5124,
            )

            return self._parent._cast(
                _5124.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5255.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5256.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(_5256.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(
                _5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5261.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(
                _5261.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5262.AssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(_5262.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5263.BearingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5265.BeltDriveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(
                _5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5268.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5269.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5270.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5271.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5273.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5273,
            )

            return self._parent._cast(_5273.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5274.BoltCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5275.BoltedJointCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5276.ClutchCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(_5276.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5278.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5281.ConceptCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(
                _5281.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5283.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(
                _5283.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5284.ConceptGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5286.ConceptGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5287.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(_5287.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5289.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5289,
            )

            return self._parent._cast(_5289.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5291.ConnectorCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(_5291.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5292.CouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(_5292.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5294.CouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5296.CVTCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(_5296.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5297.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5297,
            )

            return self._parent._cast(_5297.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5298.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5300.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5302.CylindricalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(
                _5302.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5304.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(
                _5304.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5305.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(
                _5305.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5306.DatumCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5307.ExternalCADModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(
                _5307.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5308.FaceGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(_5308.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5310.FaceGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5311.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5312.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5313.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(_5313.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5315.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(_5315.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5316.GuideDxfModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(_5316.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5317.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(_5317.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5319.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(_5319.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5321.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5323.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5324.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5326.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(
                _5326.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5327.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5329.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(
                _5329.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5330.MassDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5331.MeasurementComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(
                _5331.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5333.OilSealCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(_5333.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5335.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5337.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5339.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5340.PlanetCarrierCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(_5340.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5341.PointLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(_5341.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5342.PowerLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(_5342.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5343.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(_5343.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5344.RingPinsCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(_5344.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5346.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(
                _5346.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5347.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5349.RootAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5350.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(_5350.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5351.ShaftHubConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5354.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5356.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5357.SpringDamperCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(_5357.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5359.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5360.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5362.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5363.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5365.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5366.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5367.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5368.SynchroniserCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5369.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5370.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5370,
            )

            return self._parent._cast(
                _5370.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5371.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5372.TorqueConverterCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(
                _5372.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5374.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5375.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5376.UnbalancedMassCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5376,
            )

            return self._parent._cast(_5376.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5377.VirtualComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5378.WormGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(_5378.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5380.WormGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5380,
            )

            return self._parent._cast(_5380.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5381.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5381,
            )

            return self._parent._cast(_5381.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5383.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5383,
            )

            return self._parent._cast(
                _5383.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(
                _5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5538.AbstractShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5539.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(
                _5539.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5541.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5543.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5544.AssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(_5544.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5545.BearingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(_5545.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5547.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(_5547.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5548.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(
                _5548.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5550.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(
                _5550.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5551.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5552.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(
                _5552.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5553.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5555.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5556.BoltCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(_5556.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5557.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5558.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(_5558.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5560.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(_5560.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5562.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5563.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5565.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(
                _5565.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5566.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(
                _5566.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5568.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5569.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5571.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(
                _5571.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5573.ConnectorCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(_5573.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5574.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(_5574.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5576.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(
                _5576.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5578.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(_5578.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5579.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(_5579.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5580.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5582.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(
                _5582.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5584.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5587.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(
                _5587.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5588.DatumCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(_5588.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5589.ExternalCADModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(
                _5589.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5590.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(_5590.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5592.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5593.FEPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(_5593.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5594.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5595.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(_5595.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5597.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(_5597.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5598.GuideDxfModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5599.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(_5599.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5601.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5603.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5605.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5606.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5608.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5609.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5611.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5612.MassDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(_5612.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5613.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5614.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(
                _5614.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5615.OilSealCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5617.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(
                _5617.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5619.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5621.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5622.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5623.PointLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(_5623.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5624.PowerLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(_5624.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5625.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(_5625.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5626.RingPinsCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(_5626.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5628.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5629.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5631.RootAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5632.ShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(_5632.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5633.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5635.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5636.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5638.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5639.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5641.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5642.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5644.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5645.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5647.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5648.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5649.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5650.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5651.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5652.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(
                _5652.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5653.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5654.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5656.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5657.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5658.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5658,
            )

            return self._parent._cast(
                _5658.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5659.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5660.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5660,
            )

            return self._parent._cast(_5660.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5662.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5662,
            )

            return self._parent._cast(
                _5662.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5663.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5663,
            )

            return self._parent._cast(
                _5663.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5665.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5665,
            )

            return self._parent._cast(
                _5665.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5888.AbstractShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(_5888.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5889.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(
                _5889.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5891.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5893.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(
                _5893.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5894.AssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(_5894.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5895.BearingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BearingCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5897.BeltDriveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5898.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5898,
            )

            return self._parent._cast(
                _5898.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5900.BevelDifferentialGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(
                _5900.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5901.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(
                _5901.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5902.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(
                _5902.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5903.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.BevelGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5905.BevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5906.BoltCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5907.BoltedJointCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5908.ClutchCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5910.ClutchHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5913.ConceptCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5915.ConceptCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5916.ConceptGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5918.ConceptGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5919.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5921.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5923.ConnectorCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5924.CouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5926.CouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5928.CVTCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5929.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5930.CycloidalAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5932.CycloidalDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5934.CylindricalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5936.CylindricalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5937.CylindricalPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(
                _5937.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5938.DatumCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5939.ExternalCADModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5940.FaceGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5942.FaceGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5943.FEPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(_5943.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5944.FlexiblePinAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(_5944.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5945.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(_5945.GearCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5947.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5948.GuideDxfModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(_5948.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5949.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(_5949.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5951.HypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(_5951.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(
                _5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5955.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5956.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(
                _5956.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5958.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(
                _5958.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5959.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(
                _5959.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5961.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(
                _5961.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5962.MassDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5963.MeasurementComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(
                _5963.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5965.OilSealCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.OilSealCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5967.PartToPartShearCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(
                _5967.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5969.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(
                _5969.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5971.PlanetaryGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(_5971.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5972.PlanetCarrierCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(_5972.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5973.PointLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(_5973.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5974.PowerLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5975.PulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5976.RingPinsCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5978.RollingRingAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5979.RollingRingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.RollingRingCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5981.RootAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(_5981.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5982.ShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5983.ShaftHubConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5985.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(_5985.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5986.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(_5986.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5988.SpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(_5988.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5989.SpringDamperCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5991.SpringDamperHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5992.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(
                _5992.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5994.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5994,
            )

            return self._parent._cast(
                _5994.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5995.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5997.StraightBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(
                _5997.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5998.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(
                _5998.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5999.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(
                _5999.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6000.SynchroniserCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.SynchroniserCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6001.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6002.SynchroniserPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6003.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6004.TorqueConverterCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6006.TorqueConverterPumpCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(_6006.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6007.TorqueConverterTurbineCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6007,
            )

            return self._parent._cast(
                _6007.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6008.UnbalancedMassCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6008,
            )

            return self._parent._cast(_6008.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6009.VirtualComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(_6009.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6010.WormGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6010,
            )

            return self._parent._cast(_6010.WormGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6012.WormGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6012,
            )

            return self._parent._cast(_6012.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6013.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6013,
            )

            return self._parent._cast(_6013.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6015.ZerolBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6015,
            )

            return self._parent._cast(_6015.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6147,
            )

            return self._parent._cast(
                _6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_6153.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6154,
            )

            return self._parent._cast(
                _6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6155.BearingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BearingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6157.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6157,
            )

            return self._parent._cast(
                _6157.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6160.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6165.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6166.BoltCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.BoltCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6167.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6167,
            )

            return self._parent._cast(
                _6167.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6168.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6168,
            )

            return self._parent._cast(
                _6168.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6173.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6178.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6181.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6181,
            )

            return self._parent._cast(
                _6181.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6184.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6188.CVTCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6188,
            )

            return self._parent._cast(
                _6188.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6189,
            )

            return self._parent._cast(
                _6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6190.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6196.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6198.DatumCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.DatumCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6202.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6202,
            )

            return self._parent._cast(
                _6202.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6204.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6205.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6207.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6207,
            )

            return self._parent._cast(
                _6207.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6208,
            )

            return self._parent._cast(
                _6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6211.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6211,
            )

            return self._parent._cast(
                _6211.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6215.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6218.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6221.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6221,
            )

            return self._parent._cast(
                _6221.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6227.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6231.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6231,
            )

            return self._parent._cast(
                _6231.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6235,
            )

            return self._parent._cast(
                _6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6238.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6238,
            )

            return self._parent._cast(
                _6238.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6241.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6241,
            )

            return self._parent._cast(
                _6241.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6245.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6248.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6249.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6254.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6257.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6259,
            )

            return self._parent._cast(
                _6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6260.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6264.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6264,
            )

            return self._parent._cast(
                _6264.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6268,
            )

            return self._parent._cast(
                _6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6269,
            )

            return self._parent._cast(
                _6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6270,
            )

            return self._parent._cast(
                _6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6272.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6272,
            )

            return self._parent._cast(
                _6272.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6273,
            )

            return self._parent._cast(
                _6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6275.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6275,
            )

            return self._parent._cast(
                _6275.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6416.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6417.AbstractShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(_6417.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6418.AbstractShaftOrHousingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(
                _6418.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6420.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(
                _6420.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6422.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(
                _6422.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6423.AssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(_6423.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6424.BearingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BearingCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6426.BeltDriveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6427.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(
                _6427.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6429.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(
                _6429.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6430.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(
                _6430.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6431.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(
                _6431.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6432.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6434.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6435.BoltCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6436.BoltedJointCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6437.ClutchCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6439.ClutchHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ClutchHalfCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6442.ConceptCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6444.ConceptCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6445.ConceptGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6447.ConceptGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6448.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(_6448.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6450.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6452.ConnectorCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6453.CouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6455.CouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6457.CVTCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6458.CVTPulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6459.CycloidalAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6461.CycloidalDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6463.CylindricalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6465.CylindricalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6466.CylindricalPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(
                _6466.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6467.DatumCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6468.ExternalCADModelCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6469.FaceGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6471.FaceGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(_6471.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6472.FEPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6473.FlexiblePinAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(_6473.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6474.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.GearCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6476.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(_6476.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6477.GuideDxfModelCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(_6477.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6478.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(_6478.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6480.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6482.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6484.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6485.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(
                _6485.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6487.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6488.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(
                _6488.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6490.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6491.MassDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6492.MeasurementComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6494.OilSealCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.OilSealCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6496.PartToPartShearCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(
                _6496.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6498.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(
                _6498.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6500.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6501.PlanetCarrierCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(_6501.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6502.PointLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6503.PowerLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(_6503.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6504.PulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6505.RingPinsCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6507.RollingRingAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(_6507.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6508.RollingRingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.RollingRingCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6510.RootAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(_6510.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6511.ShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6512.ShaftHubConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6514.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6515.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(_6515.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6517.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6518.SpringDamperCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6520.SpringDamperHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6521.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(
                _6521.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6523.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(
                _6523.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6524.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6526.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6527.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(
                _6527.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6528.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6529.SynchroniserCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6530.SynchroniserHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6531.SynchroniserPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6532.SynchroniserSleeveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6533.TorqueConverterCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6535.TorqueConverterPumpCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6536.TorqueConverterTurbineCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(
                _6536.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6537.UnbalancedMassCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6537,
            )

            return self._parent._cast(_6537.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6538.VirtualComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(_6538.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6539.WormGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6539,
            )

            return self._parent._cast(_6539.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6541.WormGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6541,
            )

            return self._parent._cast(_6541.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6542.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6542,
            )

            return self._parent._cast(_6542.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6544.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6544,
            )

            return self._parent._cast(_6544.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6683.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(
                _6683.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6684.AbstractShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(_6684.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(
                _6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6689.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6690.AssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(_6690.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6691.BearingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BearingCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6693.BeltDriveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(
                _6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6696.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6697.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(
                _6697.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6698.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(
                _6698.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6699.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6701.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(_6701.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6702.BoltCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.BoltCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6703.BoltedJointCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6704.ClutchCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(_6704.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6706.ClutchHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6709.ConceptCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(
                _6709.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6711.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(
                _6711.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6712.ConceptGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6714.ConceptGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6715.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(_6715.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6717.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6719.ConnectorCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(_6719.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6720.CouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(_6720.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6722.CouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(_6722.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6724.CVTCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(_6724.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6725.CVTPulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(_6725.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6726.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(
                _6726.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6728.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6730.CylindricalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(
                _6730.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6732.CylindricalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(
                _6732.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6733.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(
                _6733.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6734.DatumCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6735.ExternalCADModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(
                _6735.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6736.FaceGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6738.FaceGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6738,
            )

            return self._parent._cast(_6738.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6739.FEPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(_6739.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6740.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6743.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(_6743.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6744.GuideDxfModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(_6744.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6745.HypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(_6745.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6747.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(_6747.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_6751.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6752.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6754.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(
                _6754.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_6755.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(
                _6755.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6757.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(
                _6757.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6758.MassDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(_6758.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6759.MeasurementComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(
                _6759.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6761.OilSealCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6763.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(
                _6763.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6765.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(
                _6765.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6767.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6768.PlanetCarrierCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6768,
            )

            return self._parent._cast(_6768.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6769.PointLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6770.PowerLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(_6770.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6771.PulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(_6771.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6772.RingPinsCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(_6772.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6774.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(
                _6774.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6775.RollingRingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6777.RootAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(_6777.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6778.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(_6778.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6779.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6781.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6782.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6784.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6785.SpringDamperCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(_6785.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6787.SpringDamperHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6790.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6791.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6793.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6794.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6795.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(
                _6795.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6796.SynchroniserCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(_6796.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6797.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6798.SynchroniserPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(
                _6798.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6799.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6800.TorqueConverterCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(
                _6800.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6802.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6803.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6804.UnbalancedMassCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6804,
            )

            return self._parent._cast(_6804.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6805.VirtualComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6806.WormGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6806,
            )

            return self._parent._cast(_6806.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6808.WormGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6808,
            )

            return self._parent._cast(_6808.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6809.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6809,
            )

            return self._parent._cast(_6809.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6811.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6811,
            )

            return self._parent._cast(
                _6811.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7150.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7151.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7151,
            )

            return self._parent._cast(
                _7151.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7153.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7155.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7155,
            )

            return self._parent._cast(
                _7155.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7157.BearingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7159.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7160.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7160,
            )

            return self._parent._cast(
                _7160.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7162.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7163.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7164.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7165.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7167.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7168.BoltCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7169.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7170.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7170,
            )

            return self._parent._cast(
                _7170.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7172.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7172,
            )

            return self._parent._cast(
                _7172.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7175.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7177.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7178.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7180.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7181.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7183.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7183,
            )

            return self._parent._cast(
                _7183.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7185.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7185,
            )

            return self._parent._cast(
                _7185.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7186.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7188,
            )

            return self._parent._cast(
                _7188.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7190.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7191.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7191,
            )

            return self._parent._cast(
                _7191.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7192.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7194.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7196.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7196,
            )

            return self._parent._cast(
                _7196.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7199.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7200.DatumCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7201.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7202.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7202,
            )

            return self._parent._cast(
                _7202.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7204.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7205.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7206.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7207.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7209.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7210.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7210,
            )

            return self._parent._cast(
                _7210.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7211.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7213.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7213,
            )

            return self._parent._cast(
                _7213.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7215.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7217.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7218.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7220.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7221.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7223.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7224.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7224,
            )

            return self._parent._cast(
                _7224.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7225.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7227.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7229.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7231.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7233.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7233,
            )

            return self._parent._cast(
                _7233.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7234.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7234,
            )

            return self._parent._cast(
                _7234.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7235.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7236.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7236,
            )

            return self._parent._cast(
                _7236.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7237.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7238.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7240.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7240,
            )

            return self._parent._cast(
                _7240.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7241.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7243.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7243,
            )

            return self._parent._cast(
                _7243.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7244.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7245.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7248.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7250.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7251.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7253.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7256.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7257.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7259.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7260.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7261.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7261,
            )

            return self._parent._cast(
                _7261.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7262.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7263.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7264.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7264,
            )

            return self._parent._cast(
                _7264.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7265.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7266.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7268.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7269.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7269,
            )

            return self._parent._cast(
                _7269.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7270.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7270,
            )

            return self._parent._cast(
                _7270.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7271.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7271,
            )

            return self._parent._cast(
                _7271.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7272.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7272,
            )

            return self._parent._cast(
                _7272.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7274.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7274,
            )

            return self._parent._cast(
                _7274.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7275.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7275,
            )

            return self._parent._cast(
                _7275.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7277.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7277,
            )

            return self._parent._cast(
                _7277.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7414.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7415.AbstractShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7416.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(
                _7416.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7418.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7420.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7421.AssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(_7421.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7422.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7424.BeltDriveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(_7424.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7425.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(
                _7425.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7427.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7428.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7429.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(
                _7429.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7430.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(_7430.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7432.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolt_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7433.BoltCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7434.BoltedJointCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(_7434.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7435.ClutchCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7437.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(_7437.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7440.ConceptCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7442.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7443.ConceptGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7445.ConceptGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7446.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(_7446.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7448.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(
                _7448.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def connector_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7450.ConnectorCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(_7450.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7451.CouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(_7451.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7453.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(
                _7453.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7455.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(_7455.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7456.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(_7456.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7457.CycloidalAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7459.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(
                _7459.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7461.CylindricalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(
                _7461.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7463.CylindricalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(
                _7463.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7464.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(
                _7464.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7465.DatumCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7466.ExternalCADModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7467.FaceGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(_7467.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7469.FaceGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(_7469.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7470.FEPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(_7470.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7471.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7472.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(_7472.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7474.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(_7474.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7475.GuideDxfModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7476.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(_7476.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7478.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7480.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7482.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7483.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7485.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7486.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7488.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7489.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(_7489.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7490.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(
                _7490.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7492.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7494.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(
                _7494.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7496.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7498.PlanetaryGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7498,
            )

            return self._parent._cast(
                _7498.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7499.PlanetCarrierCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7500.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(_7500.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7501.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(_7501.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7502.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(_7502.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7503.RingPinsCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(_7503.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7505.RollingRingAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7506.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def root_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7508.RootAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.RootAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7509.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(_7509.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7510.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7512.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7513.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7515.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7516.SpringDamperCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7518.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7519.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7521.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7522.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7524.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7525.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7526.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7527.SynchroniserCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7528.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7529.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7530.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7531.TorqueConverterCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(
                _7531.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7533.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7534.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7535.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7535,
            )

            return self._parent._cast(
                _7535.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7536.VirtualComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7537.WormGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7537,
            )

            return self._parent._cast(_7537.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7539.WormGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7539,
            )

            return self._parent._cast(_7539.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7540.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7540,
            )

            return self._parent._cast(
                _7540.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7542.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7542,
            )

            return self._parent._cast(
                _7542.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "PartCompoundAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PartCompoundAnalysis._Cast_PartCompoundAnalysis":
        return self._Cast_PartCompoundAnalysis(self)
