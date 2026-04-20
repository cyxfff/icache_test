#define _GNU_SOURCE
#include <errno.h>
#include <inttypes.h>
#include <signal.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define CONFIG_HOT_L1_SIZE 0u
#define CONFIG_HOT_L1_INSNS 0u
#define CONFIG_HOT_L1_REGION_REPS 0u
#define CONFIG_HOT_L1_POS 1u
#define CONFIG_HOT_L1_ALIGN 64u
#define CONFIG_HOT_L2_SIZE 0u
#define CONFIG_HOT_L2_INSNS 0u
#define CONFIG_HOT_L2_REGION_REPS 0u
#define CONFIG_HOT_L2_POS 7u
#define CONFIG_HOT_L2_ALIGN 64u
#define CONFIG_DATA_STREAM_SIZE 0u
#define CONFIG_DATA_STREAM_STRIDE 0u
#define CONFIG_DATA_STREAM_REGION_REPS 0u
#define CONFIG_DATA_STREAM_POS 5u
#define CONFIG_DATA_POINTER_CHASE_PAGE_COUNT 0u
#define CONFIG_DATA_POINTER_CHASE_LINES_PER_PAGE 1u
#define CONFIG_DATA_POINTER_CHASE_NODE_COUNT 0u
#define CONFIG_DATA_POINTER_CHASE_POOL_BYTES 0u
#define CONFIG_DATA_POINTER_CHASE_REGION_REPS 0u
#define CONFIG_DATA_POINTER_CHASE_POS 6u
#define CONFIG_DATA_PAGE_STRIDE_PAGE_COUNT 0u
#define CONFIG_DATA_PAGE_STRIDE_PAGE_STRIDE 1u
#define CONFIG_DATA_PAGE_STRIDE_LINE_INDEX 0u
#define CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT 0u
#define CONFIG_DATA_PAGE_STRIDE_POOL_BYTES 0u
#define CONFIG_DATA_PAGE_STRIDE_REGION_REPS 0u
#define CONFIG_DATA_PAGE_STRIDE_POS 7u
#define CONFIG_DATA_INDIRECT_GATHER_PAGE_COUNT 0u
#define CONFIG_DATA_INDIRECT_GATHER_LINES_PER_PAGE 1u
#define CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT 0u
#define CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES 0u
#define CONFIG_DATA_INDIRECT_GATHER_INDEX_STRIDE 1u
#define CONFIG_DATA_INDIRECT_GATHER_REGION_REPS 0u
#define CONFIG_DATA_INDIRECT_GATHER_POS 8u
#define CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT 128u
#define CONFIG_DATA_HOT_STRIDE_STRIDE 4u
#define CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES 512u
#define CONFIG_DATA_HOT_STRIDE_REGION_REPS 1u
#define CONFIG_DATA_HOT_STRIDE_POS 9u
#define CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT 2048u
#define CONFIG_DATA_COLD_STRIDE_STRIDE 256u
#define CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES 524036u
#define CONFIG_DATA_COLD_STRIDE_REGION_REPS 1u
#define CONFIG_DATA_COLD_STRIDE_POS 10u
#define CONFIG_DATA_TLB_INDIRECT_PAGE_COUNT 128u
#define CONFIG_DATA_TLB_INDIRECT_LINE_INDEX 0u
#define CONFIG_DATA_TLB_INDIRECT_ACCESS_COUNT 128u
#define CONFIG_DATA_TLB_INDIRECT_POOL_BYTES 524288u
#define CONFIG_DATA_TLB_INDIRECT_REGION_REPS 1u
#define CONFIG_DATA_TLB_INDIRECT_POS 11u
#define CONFIG_FETCH_TOTAL_BLOCKS 0u
#define CONFIG_FETCH_BLOCK_ALIGN 64u
#define CONFIG_FETCH_DIRECT_RUN_LEN 0u
#define CONFIG_FETCH_BRANCH_PAIRS_PER_BLOCK 0u
#define CONFIG_FETCH_BLOCK_SLOTS 16u
#define CONFIG_FETCH_REGION_REPS 0u
#define CONFIG_FETCH_POS 3u
#define CONFIG_FETCH_LAYOUT_STR "linear"
#define CONFIG_ITLB_FUNCS 0u
#define CONFIG_ITLB_LINES_PER_PAGE 1u
#define CONFIG_ITLB_REGION_REPS 0u
#define CONFIG_ITLB_FUNC_ALIGN 4096u
#define CONFIG_ITLB_DIRECT_RUN_LEN 0u
#define CONFIG_ITLB_POS 2u
#define CONFIG_ITLB_MODE_STR "chain"
#define CONFIG_CALL_RET_FUNCS 0u
#define CONFIG_CALL_RET_LINES_PER_FUNC 1u
#define CONFIG_CALL_RET_REGION_REPS 0u
#define CONFIG_CALL_RET_POS 3u
#define CONFIG_PLT_STUB_FUNCS 0u
#define CONFIG_PLT_STUB_REGION_REPS 0u
#define CONFIG_PLT_STUB_POS 4u
#define CONFIG_INDIRECT_TARGET_COUNT 0u
#define CONFIG_INDIRECT_TARGET_BLOCK_ALIGN 64u
#define CONFIG_INDIRECT_TARGET_REGION_REPS 0u
#define CONFIG_INDIRECT_TARGET_POS 5u
#define CONFIG_MAIN_TOTAL_BLOCKS 0u
#define CONFIG_MAIN_BLOCK_ALIGN 64u
#define CONFIG_MAIN_DIRECT_RUN_LEN 0u
#define CONFIG_MAIN_REGION_REPS 0u
#define CONFIG_MAIN_POS 6u
#define CONFIG_MAIN_LAYOUT_STR "in_page_shuffle"
#define CONFIG_SEED 1337u
#define CONFIG_HOT_L1_ENTRIES_PER_ITER 0u
#define CONFIG_HOT_L2_ENTRIES_PER_ITER 0u
#define CONFIG_DATA_STREAM_ACCESSES_PER_CALL 0u
#define CONFIG_DATA_STREAM_ACCESSES_PER_ITER 0u
#define CONFIG_DATA_POINTER_CHASE_NODES 0u
#define CONFIG_DATA_POINTER_CHASE_ACCESSES_PER_ITER 0u
#define CONFIG_DATA_PAGE_STRIDE_ACCESSES_PER_CALL 0u
#define CONFIG_DATA_PAGE_STRIDE_ACCESSES_PER_ITER 0u
#define CONFIG_DATA_INDIRECT_GATHER_NODES 0u
#define CONFIG_DATA_INDIRECT_GATHER_ACCESSES_PER_ITER 0u
#define CONFIG_DATA_HOT_STRIDE_ACCESSES_PER_CALL 128u
#define CONFIG_DATA_HOT_STRIDE_ACCESSES_PER_ITER 128u
#define CONFIG_DATA_COLD_STRIDE_ACCESSES_PER_CALL 2048u
#define CONFIG_DATA_COLD_STRIDE_ACCESSES_PER_ITER 2048u
#define CONFIG_DATA_TLB_INDIRECT_ACCESSES_PER_CALL 128u
#define CONFIG_DATA_TLB_INDIRECT_ACCESSES_PER_ITER 128u
#define CONFIG_FETCH_BLOCK_ENTRIES_PER_ITER 0u
#define CONFIG_ITLB_CALLS_PER_ITER 0u
#define CONFIG_CALL_RET_CALLS_PER_ITER 0u
#define CONFIG_PLT_STUB_CALLS_PER_ITER 0u
#define CONFIG_INDIRECT_TARGET_CALLS_PER_ITER 0u
#define CONFIG_MAIN_BLOCK_ENTRIES_PER_ITER 0u
#define CONFIG_TOTAL_FRONTEND_UNITS_PER_ITER 2304u
#define CONFIG_FETCH_INDIRECT_BLOCKS_PER_CHAIN 0u
#define CONFIG_MAIN_INDIRECT_BLOCKS_PER_CHAIN 0u
#define CONFIG_ITLB_INDIRECT_FUNCS_PER_CHAIN 0u
#define DEFAULT_ITERS 10000ull

static const uint32_t kMainExecSamples[1] = {
    0,
};

static const uint32_t kMainPhysicalOrder[1] = {
    0,
};

static const uint32_t kMainPhysSamples[1] = {
    0,
};

static const uint32_t kFetchPhysicalOrder[1] = {
    0,
};

static const uint32_t kItlbPhysicalOrder[1] = {
    0,
};

static const uint32_t kItlbExecOrder[1] = {
    0,
};

static const uint32_t kItlbSamples[1] = {
    0,
};

static const uint32_t kCallRetPhysicalOrder[1] = {
    0,
};

static const uint32_t kCallRetExecOrder[1] = {
    0,
};

static const uint32_t kCallRetSamples[1] = {
    0,
};

static const uint32_t kDataPointerChaseOffsets[1] = {
    0,
};

static const uint32_t kDataPageStrideOffsets[1] = {
    0,
};

static const uint32_t kDataIndirectGatherOffsets[1] = {
    0,
};

static const uint32_t kDataHotStrideOffsets[128] = {
    0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44,
    48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92,
    96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140,
    144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188,
    192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236,
    240, 244, 248, 252, 256, 260, 264, 268, 272, 276, 280, 284,
    288, 292, 296, 300, 304, 308, 312, 316, 320, 324, 328, 332,
    336, 340, 344, 348, 352, 356, 360, 364, 368, 372, 376, 380,
    384, 388, 392, 396, 400, 404, 408, 412, 416, 420, 424, 428,
    432, 436, 440, 444, 448, 452, 456, 460, 464, 468, 472, 476,
    480, 484, 488, 492, 496, 500, 504, 508,
};

static const uint32_t kDataColdStrideOffsets[2048] = {
    0, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816,
    3072, 3328, 3584, 3840, 4096, 4352, 4608, 4864, 5120, 5376, 5632, 5888,
    6144, 6400, 6656, 6912, 7168, 7424, 7680, 7936, 8192, 8448, 8704, 8960,
    9216, 9472, 9728, 9984, 10240, 10496, 10752, 11008, 11264, 11520, 11776, 12032,
    12288, 12544, 12800, 13056, 13312, 13568, 13824, 14080, 14336, 14592, 14848, 15104,
    15360, 15616, 15872, 16128, 16384, 16640, 16896, 17152, 17408, 17664, 17920, 18176,
    18432, 18688, 18944, 19200, 19456, 19712, 19968, 20224, 20480, 20736, 20992, 21248,
    21504, 21760, 22016, 22272, 22528, 22784, 23040, 23296, 23552, 23808, 24064, 24320,
    24576, 24832, 25088, 25344, 25600, 25856, 26112, 26368, 26624, 26880, 27136, 27392,
    27648, 27904, 28160, 28416, 28672, 28928, 29184, 29440, 29696, 29952, 30208, 30464,
    30720, 30976, 31232, 31488, 31744, 32000, 32256, 32512, 32768, 33024, 33280, 33536,
    33792, 34048, 34304, 34560, 34816, 35072, 35328, 35584, 35840, 36096, 36352, 36608,
    36864, 37120, 37376, 37632, 37888, 38144, 38400, 38656, 38912, 39168, 39424, 39680,
    39936, 40192, 40448, 40704, 40960, 41216, 41472, 41728, 41984, 42240, 42496, 42752,
    43008, 43264, 43520, 43776, 44032, 44288, 44544, 44800, 45056, 45312, 45568, 45824,
    46080, 46336, 46592, 46848, 47104, 47360, 47616, 47872, 48128, 48384, 48640, 48896,
    49152, 49408, 49664, 49920, 50176, 50432, 50688, 50944, 51200, 51456, 51712, 51968,
    52224, 52480, 52736, 52992, 53248, 53504, 53760, 54016, 54272, 54528, 54784, 55040,
    55296, 55552, 55808, 56064, 56320, 56576, 56832, 57088, 57344, 57600, 57856, 58112,
    58368, 58624, 58880, 59136, 59392, 59648, 59904, 60160, 60416, 60672, 60928, 61184,
    61440, 61696, 61952, 62208, 62464, 62720, 62976, 63232, 63488, 63744, 64000, 64256,
    64512, 64768, 65024, 65280, 65536, 65792, 66048, 66304, 66560, 66816, 67072, 67328,
    67584, 67840, 68096, 68352, 68608, 68864, 69120, 69376, 69632, 69888, 70144, 70400,
    70656, 70912, 71168, 71424, 71680, 71936, 72192, 72448, 72704, 72960, 73216, 73472,
    73728, 73984, 74240, 74496, 74752, 75008, 75264, 75520, 75776, 76032, 76288, 76544,
    76800, 77056, 77312, 77568, 77824, 78080, 78336, 78592, 78848, 79104, 79360, 79616,
    79872, 80128, 80384, 80640, 80896, 81152, 81408, 81664, 81920, 82176, 82432, 82688,
    82944, 83200, 83456, 83712, 83968, 84224, 84480, 84736, 84992, 85248, 85504, 85760,
    86016, 86272, 86528, 86784, 87040, 87296, 87552, 87808, 88064, 88320, 88576, 88832,
    89088, 89344, 89600, 89856, 90112, 90368, 90624, 90880, 91136, 91392, 91648, 91904,
    92160, 92416, 92672, 92928, 93184, 93440, 93696, 93952, 94208, 94464, 94720, 94976,
    95232, 95488, 95744, 96000, 96256, 96512, 96768, 97024, 97280, 97536, 97792, 98048,
    98304, 98560, 98816, 99072, 99328, 99584, 99840, 100096, 100352, 100608, 100864, 101120,
    101376, 101632, 101888, 102144, 102400, 102656, 102912, 103168, 103424, 103680, 103936, 104192,
    104448, 104704, 104960, 105216, 105472, 105728, 105984, 106240, 106496, 106752, 107008, 107264,
    107520, 107776, 108032, 108288, 108544, 108800, 109056, 109312, 109568, 109824, 110080, 110336,
    110592, 110848, 111104, 111360, 111616, 111872, 112128, 112384, 112640, 112896, 113152, 113408,
    113664, 113920, 114176, 114432, 114688, 114944, 115200, 115456, 115712, 115968, 116224, 116480,
    116736, 116992, 117248, 117504, 117760, 118016, 118272, 118528, 118784, 119040, 119296, 119552,
    119808, 120064, 120320, 120576, 120832, 121088, 121344, 121600, 121856, 122112, 122368, 122624,
    122880, 123136, 123392, 123648, 123904, 124160, 124416, 124672, 124928, 125184, 125440, 125696,
    125952, 126208, 126464, 126720, 126976, 127232, 127488, 127744, 128000, 128256, 128512, 128768,
    129024, 129280, 129536, 129792, 130048, 130304, 130560, 130816, 131072, 131328, 131584, 131840,
    132096, 132352, 132608, 132864, 133120, 133376, 133632, 133888, 134144, 134400, 134656, 134912,
    135168, 135424, 135680, 135936, 136192, 136448, 136704, 136960, 137216, 137472, 137728, 137984,
    138240, 138496, 138752, 139008, 139264, 139520, 139776, 140032, 140288, 140544, 140800, 141056,
    141312, 141568, 141824, 142080, 142336, 142592, 142848, 143104, 143360, 143616, 143872, 144128,
    144384, 144640, 144896, 145152, 145408, 145664, 145920, 146176, 146432, 146688, 146944, 147200,
    147456, 147712, 147968, 148224, 148480, 148736, 148992, 149248, 149504, 149760, 150016, 150272,
    150528, 150784, 151040, 151296, 151552, 151808, 152064, 152320, 152576, 152832, 153088, 153344,
    153600, 153856, 154112, 154368, 154624, 154880, 155136, 155392, 155648, 155904, 156160, 156416,
    156672, 156928, 157184, 157440, 157696, 157952, 158208, 158464, 158720, 158976, 159232, 159488,
    159744, 160000, 160256, 160512, 160768, 161024, 161280, 161536, 161792, 162048, 162304, 162560,
    162816, 163072, 163328, 163584, 163840, 164096, 164352, 164608, 164864, 165120, 165376, 165632,
    165888, 166144, 166400, 166656, 166912, 167168, 167424, 167680, 167936, 168192, 168448, 168704,
    168960, 169216, 169472, 169728, 169984, 170240, 170496, 170752, 171008, 171264, 171520, 171776,
    172032, 172288, 172544, 172800, 173056, 173312, 173568, 173824, 174080, 174336, 174592, 174848,
    175104, 175360, 175616, 175872, 176128, 176384, 176640, 176896, 177152, 177408, 177664, 177920,
    178176, 178432, 178688, 178944, 179200, 179456, 179712, 179968, 180224, 180480, 180736, 180992,
    181248, 181504, 181760, 182016, 182272, 182528, 182784, 183040, 183296, 183552, 183808, 184064,
    184320, 184576, 184832, 185088, 185344, 185600, 185856, 186112, 186368, 186624, 186880, 187136,
    187392, 187648, 187904, 188160, 188416, 188672, 188928, 189184, 189440, 189696, 189952, 190208,
    190464, 190720, 190976, 191232, 191488, 191744, 192000, 192256, 192512, 192768, 193024, 193280,
    193536, 193792, 194048, 194304, 194560, 194816, 195072, 195328, 195584, 195840, 196096, 196352,
    196608, 196864, 197120, 197376, 197632, 197888, 198144, 198400, 198656, 198912, 199168, 199424,
    199680, 199936, 200192, 200448, 200704, 200960, 201216, 201472, 201728, 201984, 202240, 202496,
    202752, 203008, 203264, 203520, 203776, 204032, 204288, 204544, 204800, 205056, 205312, 205568,
    205824, 206080, 206336, 206592, 206848, 207104, 207360, 207616, 207872, 208128, 208384, 208640,
    208896, 209152, 209408, 209664, 209920, 210176, 210432, 210688, 210944, 211200, 211456, 211712,
    211968, 212224, 212480, 212736, 212992, 213248, 213504, 213760, 214016, 214272, 214528, 214784,
    215040, 215296, 215552, 215808, 216064, 216320, 216576, 216832, 217088, 217344, 217600, 217856,
    218112, 218368, 218624, 218880, 219136, 219392, 219648, 219904, 220160, 220416, 220672, 220928,
    221184, 221440, 221696, 221952, 222208, 222464, 222720, 222976, 223232, 223488, 223744, 224000,
    224256, 224512, 224768, 225024, 225280, 225536, 225792, 226048, 226304, 226560, 226816, 227072,
    227328, 227584, 227840, 228096, 228352, 228608, 228864, 229120, 229376, 229632, 229888, 230144,
    230400, 230656, 230912, 231168, 231424, 231680, 231936, 232192, 232448, 232704, 232960, 233216,
    233472, 233728, 233984, 234240, 234496, 234752, 235008, 235264, 235520, 235776, 236032, 236288,
    236544, 236800, 237056, 237312, 237568, 237824, 238080, 238336, 238592, 238848, 239104, 239360,
    239616, 239872, 240128, 240384, 240640, 240896, 241152, 241408, 241664, 241920, 242176, 242432,
    242688, 242944, 243200, 243456, 243712, 243968, 244224, 244480, 244736, 244992, 245248, 245504,
    245760, 246016, 246272, 246528, 246784, 247040, 247296, 247552, 247808, 248064, 248320, 248576,
    248832, 249088, 249344, 249600, 249856, 250112, 250368, 250624, 250880, 251136, 251392, 251648,
    251904, 252160, 252416, 252672, 252928, 253184, 253440, 253696, 253952, 254208, 254464, 254720,
    254976, 255232, 255488, 255744, 256000, 256256, 256512, 256768, 257024, 257280, 257536, 257792,
    258048, 258304, 258560, 258816, 259072, 259328, 259584, 259840, 260096, 260352, 260608, 260864,
    261120, 261376, 261632, 261888, 262144, 262400, 262656, 262912, 263168, 263424, 263680, 263936,
    264192, 264448, 264704, 264960, 265216, 265472, 265728, 265984, 266240, 266496, 266752, 267008,
    267264, 267520, 267776, 268032, 268288, 268544, 268800, 269056, 269312, 269568, 269824, 270080,
    270336, 270592, 270848, 271104, 271360, 271616, 271872, 272128, 272384, 272640, 272896, 273152,
    273408, 273664, 273920, 274176, 274432, 274688, 274944, 275200, 275456, 275712, 275968, 276224,
    276480, 276736, 276992, 277248, 277504, 277760, 278016, 278272, 278528, 278784, 279040, 279296,
    279552, 279808, 280064, 280320, 280576, 280832, 281088, 281344, 281600, 281856, 282112, 282368,
    282624, 282880, 283136, 283392, 283648, 283904, 284160, 284416, 284672, 284928, 285184, 285440,
    285696, 285952, 286208, 286464, 286720, 286976, 287232, 287488, 287744, 288000, 288256, 288512,
    288768, 289024, 289280, 289536, 289792, 290048, 290304, 290560, 290816, 291072, 291328, 291584,
    291840, 292096, 292352, 292608, 292864, 293120, 293376, 293632, 293888, 294144, 294400, 294656,
    294912, 295168, 295424, 295680, 295936, 296192, 296448, 296704, 296960, 297216, 297472, 297728,
    297984, 298240, 298496, 298752, 299008, 299264, 299520, 299776, 300032, 300288, 300544, 300800,
    301056, 301312, 301568, 301824, 302080, 302336, 302592, 302848, 303104, 303360, 303616, 303872,
    304128, 304384, 304640, 304896, 305152, 305408, 305664, 305920, 306176, 306432, 306688, 306944,
    307200, 307456, 307712, 307968, 308224, 308480, 308736, 308992, 309248, 309504, 309760, 310016,
    310272, 310528, 310784, 311040, 311296, 311552, 311808, 312064, 312320, 312576, 312832, 313088,
    313344, 313600, 313856, 314112, 314368, 314624, 314880, 315136, 315392, 315648, 315904, 316160,
    316416, 316672, 316928, 317184, 317440, 317696, 317952, 318208, 318464, 318720, 318976, 319232,
    319488, 319744, 320000, 320256, 320512, 320768, 321024, 321280, 321536, 321792, 322048, 322304,
    322560, 322816, 323072, 323328, 323584, 323840, 324096, 324352, 324608, 324864, 325120, 325376,
    325632, 325888, 326144, 326400, 326656, 326912, 327168, 327424, 327680, 327936, 328192, 328448,
    328704, 328960, 329216, 329472, 329728, 329984, 330240, 330496, 330752, 331008, 331264, 331520,
    331776, 332032, 332288, 332544, 332800, 333056, 333312, 333568, 333824, 334080, 334336, 334592,
    334848, 335104, 335360, 335616, 335872, 336128, 336384, 336640, 336896, 337152, 337408, 337664,
    337920, 338176, 338432, 338688, 338944, 339200, 339456, 339712, 339968, 340224, 340480, 340736,
    340992, 341248, 341504, 341760, 342016, 342272, 342528, 342784, 343040, 343296, 343552, 343808,
    344064, 344320, 344576, 344832, 345088, 345344, 345600, 345856, 346112, 346368, 346624, 346880,
    347136, 347392, 347648, 347904, 348160, 348416, 348672, 348928, 349184, 349440, 349696, 349952,
    350208, 350464, 350720, 350976, 351232, 351488, 351744, 352000, 352256, 352512, 352768, 353024,
    353280, 353536, 353792, 354048, 354304, 354560, 354816, 355072, 355328, 355584, 355840, 356096,
    356352, 356608, 356864, 357120, 357376, 357632, 357888, 358144, 358400, 358656, 358912, 359168,
    359424, 359680, 359936, 360192, 360448, 360704, 360960, 361216, 361472, 361728, 361984, 362240,
    362496, 362752, 363008, 363264, 363520, 363776, 364032, 364288, 364544, 364800, 365056, 365312,
    365568, 365824, 366080, 366336, 366592, 366848, 367104, 367360, 367616, 367872, 368128, 368384,
    368640, 368896, 369152, 369408, 369664, 369920, 370176, 370432, 370688, 370944, 371200, 371456,
    371712, 371968, 372224, 372480, 372736, 372992, 373248, 373504, 373760, 374016, 374272, 374528,
    374784, 375040, 375296, 375552, 375808, 376064, 376320, 376576, 376832, 377088, 377344, 377600,
    377856, 378112, 378368, 378624, 378880, 379136, 379392, 379648, 379904, 380160, 380416, 380672,
    380928, 381184, 381440, 381696, 381952, 382208, 382464, 382720, 382976, 383232, 383488, 383744,
    384000, 384256, 384512, 384768, 385024, 385280, 385536, 385792, 386048, 386304, 386560, 386816,
    387072, 387328, 387584, 387840, 388096, 388352, 388608, 388864, 389120, 389376, 389632, 389888,
    390144, 390400, 390656, 390912, 391168, 391424, 391680, 391936, 392192, 392448, 392704, 392960,
    393216, 393472, 393728, 393984, 394240, 394496, 394752, 395008, 395264, 395520, 395776, 396032,
    396288, 396544, 396800, 397056, 397312, 397568, 397824, 398080, 398336, 398592, 398848, 399104,
    399360, 399616, 399872, 400128, 400384, 400640, 400896, 401152, 401408, 401664, 401920, 402176,
    402432, 402688, 402944, 403200, 403456, 403712, 403968, 404224, 404480, 404736, 404992, 405248,
    405504, 405760, 406016, 406272, 406528, 406784, 407040, 407296, 407552, 407808, 408064, 408320,
    408576, 408832, 409088, 409344, 409600, 409856, 410112, 410368, 410624, 410880, 411136, 411392,
    411648, 411904, 412160, 412416, 412672, 412928, 413184, 413440, 413696, 413952, 414208, 414464,
    414720, 414976, 415232, 415488, 415744, 416000, 416256, 416512, 416768, 417024, 417280, 417536,
    417792, 418048, 418304, 418560, 418816, 419072, 419328, 419584, 419840, 420096, 420352, 420608,
    420864, 421120, 421376, 421632, 421888, 422144, 422400, 422656, 422912, 423168, 423424, 423680,
    423936, 424192, 424448, 424704, 424960, 425216, 425472, 425728, 425984, 426240, 426496, 426752,
    427008, 427264, 427520, 427776, 428032, 428288, 428544, 428800, 429056, 429312, 429568, 429824,
    430080, 430336, 430592, 430848, 431104, 431360, 431616, 431872, 432128, 432384, 432640, 432896,
    433152, 433408, 433664, 433920, 434176, 434432, 434688, 434944, 435200, 435456, 435712, 435968,
    436224, 436480, 436736, 436992, 437248, 437504, 437760, 438016, 438272, 438528, 438784, 439040,
    439296, 439552, 439808, 440064, 440320, 440576, 440832, 441088, 441344, 441600, 441856, 442112,
    442368, 442624, 442880, 443136, 443392, 443648, 443904, 444160, 444416, 444672, 444928, 445184,
    445440, 445696, 445952, 446208, 446464, 446720, 446976, 447232, 447488, 447744, 448000, 448256,
    448512, 448768, 449024, 449280, 449536, 449792, 450048, 450304, 450560, 450816, 451072, 451328,
    451584, 451840, 452096, 452352, 452608, 452864, 453120, 453376, 453632, 453888, 454144, 454400,
    454656, 454912, 455168, 455424, 455680, 455936, 456192, 456448, 456704, 456960, 457216, 457472,
    457728, 457984, 458240, 458496, 458752, 459008, 459264, 459520, 459776, 460032, 460288, 460544,
    460800, 461056, 461312, 461568, 461824, 462080, 462336, 462592, 462848, 463104, 463360, 463616,
    463872, 464128, 464384, 464640, 464896, 465152, 465408, 465664, 465920, 466176, 466432, 466688,
    466944, 467200, 467456, 467712, 467968, 468224, 468480, 468736, 468992, 469248, 469504, 469760,
    470016, 470272, 470528, 470784, 471040, 471296, 471552, 471808, 472064, 472320, 472576, 472832,
    473088, 473344, 473600, 473856, 474112, 474368, 474624, 474880, 475136, 475392, 475648, 475904,
    476160, 476416, 476672, 476928, 477184, 477440, 477696, 477952, 478208, 478464, 478720, 478976,
    479232, 479488, 479744, 480000, 480256, 480512, 480768, 481024, 481280, 481536, 481792, 482048,
    482304, 482560, 482816, 483072, 483328, 483584, 483840, 484096, 484352, 484608, 484864, 485120,
    485376, 485632, 485888, 486144, 486400, 486656, 486912, 487168, 487424, 487680, 487936, 488192,
    488448, 488704, 488960, 489216, 489472, 489728, 489984, 490240, 490496, 490752, 491008, 491264,
    491520, 491776, 492032, 492288, 492544, 492800, 493056, 493312, 493568, 493824, 494080, 494336,
    494592, 494848, 495104, 495360, 495616, 495872, 496128, 496384, 496640, 496896, 497152, 497408,
    497664, 497920, 498176, 498432, 498688, 498944, 499200, 499456, 499712, 499968, 500224, 500480,
    500736, 500992, 501248, 501504, 501760, 502016, 502272, 502528, 502784, 503040, 503296, 503552,
    503808, 504064, 504320, 504576, 504832, 505088, 505344, 505600, 505856, 506112, 506368, 506624,
    506880, 507136, 507392, 507648, 507904, 508160, 508416, 508672, 508928, 509184, 509440, 509696,
    509952, 510208, 510464, 510720, 510976, 511232, 511488, 511744, 512000, 512256, 512512, 512768,
    513024, 513280, 513536, 513792, 514048, 514304, 514560, 514816, 515072, 515328, 515584, 515840,
    516096, 516352, 516608, 516864, 517120, 517376, 517632, 517888, 518144, 518400, 518656, 518912,
    519168, 519424, 519680, 519936, 520192, 520448, 520704, 520960, 521216, 521472, 521728, 521984,
    522240, 522496, 522752, 523008, 523264, 523520, 523776, 524032,
};

static const uint32_t kDataTlbIndirectOffsets[128] = {
    167936, 225280, 159744, 507904, 356352, 184320, 495616, 245760, 229376, 360448, 176128, 499712,
    188416, 86016, 339968, 294912, 270336, 73728, 90112, 36864, 315392, 413696, 126976, 262144,
    438272, 122880, 16384, 520192, 430080, 409600, 94208, 479232, 483328, 8192, 335872, 319488,
    487424, 258048, 151552, 102400, 278528, 212992, 0, 376832, 49152, 28672, 106496, 352256,
    45056, 274432, 475136, 24576, 114688, 233472, 40960, 208896, 65536, 503808, 61440, 417792,
    221184, 454656, 20480, 331776, 516096, 57344, 471040, 241664, 380928, 364544, 249856, 512000,
    372736, 462848, 389120, 147456, 491520, 172032, 110592, 446464, 139264, 69632, 286720, 282624,
    77824, 135168, 401408, 81920, 450560, 344064, 163840, 118784, 200704, 143360, 323584, 32768,
    196608, 327680, 253952, 442368, 217088, 155648, 405504, 307200, 204800, 466944, 385024, 290816,
    237568, 458752, 434176, 192512, 53248, 425984, 303104, 131072, 397312, 348160, 98304, 311296,
    4096, 393216, 12288, 368640, 180224, 299008, 421888, 266240,
};

static uint8_t g_data_stream_buf[CONFIG_DATA_STREAM_SIZE > 0 ? CONFIG_DATA_STREAM_SIZE : 64u] __attribute__((aligned(64)));
static uint64_t g_data_stream_sink = 0;

static uint8_t g_data_pointer_chase_pool[CONFIG_DATA_POINTER_CHASE_POOL_BYTES > 0 ? CONFIG_DATA_POINTER_CHASE_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint32_t g_data_pointer_chase_cursor = 0;
static uint64_t g_data_pointer_chase_sink = 0;

static uint8_t g_data_page_stride_buf[CONFIG_DATA_PAGE_STRIDE_POOL_BYTES > 0 ? CONFIG_DATA_PAGE_STRIDE_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint64_t g_data_page_stride_sink = 0;

static uint8_t g_data_indirect_gather_pool[CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES > 0 ? CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint32_t g_data_indirect_gather_next[CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT > 0 ? CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT : 1u];
static uint32_t g_data_indirect_gather_offsets[CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT > 0 ? CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT : 1u];
static uint32_t g_data_indirect_gather_cursor = 0;
static uint64_t g_data_indirect_gather_sink = 0;

static uint8_t g_data_hot_stride_buf[CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES > 0 ? CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES : 64u] __attribute__((aligned(64)));
static uint64_t g_data_hot_stride_sink = 0;

static uint8_t g_data_cold_stride_buf[CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES > 0 ? CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES : 64u] __attribute__((aligned(4096)));
static uint64_t g_data_cold_stride_sink = 0;

static uint8_t g_data_tlb_indirect_buf[CONFIG_DATA_TLB_INDIRECT_POOL_BYTES > 0 ? CONFIG_DATA_TLB_INDIRECT_POOL_BYTES : 64u] __attribute__((aligned(4096)));
static uint64_t g_data_tlb_indirect_sink = 0;

typedef void (*bench_func_t)(void);

static void *g_itlb_func_table[CONFIG_ITLB_FUNCS > 0 ? CONFIG_ITLB_FUNCS : 1u];
static void *g_fetch_table[CONFIG_FETCH_TOTAL_BLOCKS > 0 ? CONFIG_FETCH_TOTAL_BLOCKS : 1u];
static void *g_main_table[CONFIG_MAIN_TOTAL_BLOCKS > 0 ? CONFIG_MAIN_TOTAL_BLOCKS : 1u];
static void *g_indirect_target_table[CONFIG_INDIRECT_TARGET_COUNT > 0 ? CONFIG_INDIRECT_TARGET_COUNT : 1u];

__attribute__((used, noinline))
static void dispatch_fetch_indirect(uint64_t idx) {
    ((bench_func_t)g_fetch_table[idx])();
}

__attribute__((used, noinline))
static void dispatch_main_indirect(uint64_t idx) {
    ((bench_func_t)g_main_table[idx])();
}

__attribute__((used, noinline))
static void init_data_stream_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_STREAM_SIZE; ++idx) {
        g_data_stream_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_stream_kernel(void) {
    if (CONFIG_DATA_STREAM_SIZE == 0) return;
    uint64_t acc = g_data_stream_sink;
    for (uint32_t offset = 0; offset < CONFIG_DATA_STREAM_SIZE; offset += CONFIG_DATA_STREAM_STRIDE) {
        acc += *(const volatile uint64_t *)(g_data_stream_buf + offset);
    }
    g_data_stream_sink = acc;
}

__attribute__((used, noinline))
static void init_data_pointer_chase_pool(void) {
    if (CONFIG_DATA_POINTER_CHASE_NODE_COUNT == 0) return;
    for (uint32_t idx = 0; idx < CONFIG_DATA_POINTER_CHASE_NODE_COUNT; ++idx) {
        uint32_t cur = kDataPointerChaseOffsets[idx];
        uint32_t nxt = kDataPointerChaseOffsets[(idx + 1) % CONFIG_DATA_POINTER_CHASE_NODE_COUNT];
        *(uint32_t *)(g_data_pointer_chase_pool + cur) = nxt;
        *(uint64_t *)(g_data_pointer_chase_pool + cur + 8u) = (uint64_t)(cur ^ nxt ^ CONFIG_SEED) + (uint64_t)(idx + 1u);
    }
    g_data_pointer_chase_cursor = kDataPointerChaseOffsets[0];
}

__attribute__((used, noinline))
static void data_pointer_chase_kernel(void) {
    if (CONFIG_DATA_POINTER_CHASE_NODE_COUNT == 0) return;
    uint32_t offset = g_data_pointer_chase_cursor;
    uint64_t acc = g_data_pointer_chase_sink;
    for (uint32_t step = 0; step < CONFIG_DATA_POINTER_CHASE_NODE_COUNT; ++step) {
        offset = *(volatile uint32_t *)(g_data_pointer_chase_pool + offset);
        acc += *(volatile uint64_t *)(g_data_pointer_chase_pool + offset + 8u);
    }
    g_data_pointer_chase_cursor = offset;
    g_data_pointer_chase_sink = acc;
}

__attribute__((used, noinline))
static void init_data_page_stride_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_PAGE_STRIDE_POOL_BYTES; ++idx) {
        g_data_page_stride_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_page_stride_kernel(void) {
    if (CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT == 0) return;
    uint64_t acc = g_data_page_stride_sink;
    for (uint32_t idx = 0; idx < CONFIG_DATA_PAGE_STRIDE_OFFSET_COUNT; ++idx) {
        uint32_t offset = kDataPageStrideOffsets[idx];
        acc += *(const volatile uint64_t *)(g_data_page_stride_buf + offset);
    }
    g_data_page_stride_sink = acc;
}

__attribute__((used, noinline))
static void init_data_indirect_gather_pool(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_INDIRECT_GATHER_POOL_BYTES; ++idx) {
        g_data_indirect_gather_pool[idx] = (uint8_t)(((idx * 29u) + CONFIG_SEED) & 0xFFu);
    }
    if (CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT == 0) return;
    for (uint32_t idx = 0; idx < CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT; ++idx) {
        uint32_t offset = kDataIndirectGatherOffsets[idx];
        g_data_indirect_gather_offsets[idx] = offset;
        g_data_indirect_gather_next[idx] = (idx + CONFIG_DATA_INDIRECT_GATHER_INDEX_STRIDE) % CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT;
        *(uint64_t *)(g_data_indirect_gather_pool + offset + 8u) = (uint64_t)(offset ^ CONFIG_SEED) + (uint64_t)(idx + 1u);
    }
    g_data_indirect_gather_cursor = 0;
}

__attribute__((used, noinline))
static void data_indirect_gather_kernel(void) {
    if (CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT == 0) return;
    uint32_t idx = g_data_indirect_gather_cursor;
    uint64_t acc = g_data_indirect_gather_sink;
    for (uint32_t step = 0; step < CONFIG_DATA_INDIRECT_GATHER_NODE_COUNT; ++step) {
        idx = *(volatile uint32_t *)(g_data_indirect_gather_next + idx);
        uint32_t offset = *(volatile uint32_t *)(g_data_indirect_gather_offsets + idx);
        acc += *(volatile uint64_t *)(g_data_indirect_gather_pool + offset + 8u);
    }
    g_data_indirect_gather_cursor = idx;
    g_data_indirect_gather_sink = acc;
}

__attribute__((used, noinline))
static void init_data_hot_stride_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_HOT_STRIDE_BUFFER_BYTES; ++idx) {
        g_data_hot_stride_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_hot_stride_kernel(void) {
    if (CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT == 0) return;
#if defined(__aarch64__)
    const uint8_t *base = g_data_hot_stride_buf;
    const uint32_t *offsets = kDataHotStrideOffsets;
    uint64_t acc = g_data_hot_stride_sink;
    uint64_t count = (uint64_t)CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT;
    asm volatile(
        "mov x9, xzr\n\t"
        "mov x10, %[acc]\n\t"
        "1:\n\t"
        "ldr w11, [%[offsets], x9, lsl #2]\n\t"
        "ldr w12, [%[base], x11]\n\t"
        "add x10, x10, x12\n\t"
        "add x9, x9, #1\n\t"
        "cmp x9, %[count]\n\t"
        "b.lo 1b\n\t"
        "mov %[acc], x10\n\t"
        : [acc] "+r"(acc)
        : [base] "r"(base), [offsets] "r"(offsets), [count] "r"(count)
        : "x9", "x10", "x11", "x12", "cc", "memory");
    g_data_hot_stride_sink = acc;
#else
    uint64_t acc = g_data_hot_stride_sink;
    for (uint32_t idx = 0; idx < CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT; ++idx) {
        uint32_t offset = kDataHotStrideOffsets[idx];
        acc += *(const volatile uint32_t *)(g_data_hot_stride_buf + offset);
    }
    g_data_hot_stride_sink = acc;
#endif
}

__attribute__((used, noinline))
static void init_data_cold_stride_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_COLD_STRIDE_BUFFER_BYTES; ++idx) {
        g_data_cold_stride_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_cold_stride_kernel(void) {
    if (CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT == 0) return;
#if defined(__aarch64__)
    const uint8_t *base = g_data_cold_stride_buf;
    const uint32_t *offsets = kDataColdStrideOffsets;
    uint64_t acc = g_data_cold_stride_sink;
    uint64_t count = (uint64_t)CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT;
    asm volatile(
        "mov x9, xzr\n\t"
        "mov x10, %[acc]\n\t"
        "1:\n\t"
        "ldr w11, [%[offsets], x9, lsl #2]\n\t"
        "ldr w12, [%[base], x11]\n\t"
        "add x10, x10, x12\n\t"
        "add x9, x9, #1\n\t"
        "cmp x9, %[count]\n\t"
        "b.lo 1b\n\t"
        "mov %[acc], x10\n\t"
        : [acc] "+r"(acc)
        : [base] "r"(base), [offsets] "r"(offsets), [count] "r"(count)
        : "x9", "x10", "x11", "x12", "cc", "memory");
    g_data_cold_stride_sink = acc;
#else
    uint64_t acc = g_data_cold_stride_sink;
    for (uint32_t idx = 0; idx < CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT; ++idx) {
        uint32_t offset = kDataColdStrideOffsets[idx];
        acc += *(const volatile uint32_t *)(g_data_cold_stride_buf + offset);
    }
    g_data_cold_stride_sink = acc;
#endif
}

__attribute__((used, noinline))
static void init_data_tlb_indirect_buffer(void) {
    for (uint32_t idx = 0; idx < CONFIG_DATA_TLB_INDIRECT_POOL_BYTES; ++idx) {
        g_data_tlb_indirect_buf[idx] = (uint8_t)(((idx * 131u) + CONFIG_SEED) & 0xFFu);
    }
}

__attribute__((used, noinline))
static void data_tlb_indirect_kernel(void) {
    if (CONFIG_DATA_TLB_INDIRECT_ACCESS_COUNT == 0) return;
#if defined(__aarch64__)
    const uint8_t *base = g_data_tlb_indirect_buf;
    const uint32_t *offsets = kDataTlbIndirectOffsets;
    uint64_t acc = g_data_tlb_indirect_sink;
    uint64_t count = (uint64_t)CONFIG_DATA_TLB_INDIRECT_ACCESS_COUNT;
    asm volatile(
        "mov x9, xzr\n\t"
        "mov x10, %[acc]\n\t"
        "1:\n\t"
        "ldr w11, [%[offsets], x9, lsl #2]\n\t"
        "ldr w12, [%[base], x11]\n\t"
        "add x10, x10, x12\n\t"
        "add x9, x9, #1\n\t"
        "cmp x9, %[count]\n\t"
        "b.lo 1b\n\t"
        "mov %[acc], x10\n\t"
        : [acc] "+r"(acc)
        : [base] "r"(base), [offsets] "r"(offsets), [count] "r"(count)
        : "x9", "x10", "x11", "x12", "cc", "memory");
    g_data_tlb_indirect_sink = acc;
#else
    uint64_t acc = g_data_tlb_indirect_sink;
    for (uint32_t idx = 0; idx < CONFIG_DATA_TLB_INDIRECT_ACCESS_COUNT; ++idx) {
        uint32_t offset = kDataTlbIndirectOffsets[idx];
        acc += *(const volatile uint32_t *)(g_data_tlb_indirect_buf + offset);
    }
    g_data_tlb_indirect_sink = acc;
#endif
}

__attribute__((used, noinline))
static void run_hot_l1_once(void) {
}

__attribute__((used, noinline))
static void run_hot_l2_once(void) {
}

__attribute__((used, noinline))
static void run_fetch_amplifier_once(void) {
}

__attribute__((used, noinline))
static void run_data_stream_once(void) {
}

__attribute__((used, noinline))
static void run_data_pointer_chase_once(void) {
}

__attribute__((used, noinline))
static void run_data_page_stride_once(void) {
}

__attribute__((used, noinline))
static void run_data_indirect_gather_once(void) {
}

__attribute__((used, noinline))
static void run_data_hot_stride_once(void) {
    data_hot_stride_kernel();
}

__attribute__((used, noinline))
static void run_data_cold_stride_once(void) {
    data_cold_stride_kernel();
}

__attribute__((used, noinline))
static void run_data_tlb_indirect_once(void) {
    data_tlb_indirect_kernel();
}

__attribute__((used, noinline))
static void run_itlb_region_once(void) {
}

__attribute__((used, noinline))
static void run_call_ret_chain_once(void) {
}

__attribute__((used, noinline))
static void run_plt_stub_chain_once(void) {
}

__attribute__((used, noinline))
static void run_indirect_target_set_once(void) {
}

__attribute__((used, noinline))
static void run_block_loop_once(void) {
}

static volatile sig_atomic_t g_start = 0;
static volatile sig_atomic_t g_abort = 0;

static void on_start(int signo) {
    (void)signo;
    g_start = 1;
}

static void on_abort(int signo) {
    (void)signo;
    g_abort = 1;
}

static uint64_t parse_u64(const char *text, uint64_t fallback) {
    if (!text || !*text) return fallback;
    errno = 0;
    char *end = NULL;
    unsigned long long value = strtoull(text, &end, 10);
    if (errno != 0 || !end || *end != '\0') {
        return fallback;
    }
    return (uint64_t)value;
}

static void wait_for_start_signal(void) {
    sigset_t mask;
    sigemptyset(&mask);
    while (!g_start && !g_abort) {
        sigsuspend(&mask);
    }
}

int main(int argc, char **argv) {
    struct sigaction sa_start;
    struct sigaction sa_abort;
    sa_start.sa_handler = on_start;
    sigemptyset(&sa_start.sa_mask);
    sa_start.sa_flags = 0;
    sa_abort.sa_handler = on_abort;
    sigemptyset(&sa_abort.sa_mask);
    sa_abort.sa_flags = 0;
    sigaction(SIGUSR1, &sa_start, NULL);
    sigaction(SIGTERM, &sa_abort, NULL);
    sigaction(SIGINT, &sa_abort, NULL);

    uint64_t iters = DEFAULT_ITERS;
    if (argc > 1) iters = parse_u64(argv[1], iters);
    if (iters == 0) iters = 1;

    g_itlb_func_table[0] = NULL;

    g_fetch_table[0] = NULL;

    g_main_table[0] = NULL;

    g_indirect_target_table[0] = NULL;

    init_data_hot_stride_buffer();
    init_data_cold_stride_buffer();
    init_data_tlb_indirect_buffer();

    fflush(stdout);
    puts("PROXYBENCH_READY");
    fflush(stdout);
    wait_for_start_signal();
    struct timespec bench_start;
    struct timespec bench_end;
    clock_gettime(CLOCK_MONOTONIC, &bench_start);
    uint64_t completed_iters = 0;
    while (!g_abort && completed_iters < iters) {
        for (uint32_t rep = 0; rep < CONFIG_HOT_L1_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L1_SIZE > 0) run_hot_l1_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_ITLB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_ITLB_FUNCS > 0) run_itlb_region_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_CALL_RET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_CALL_RET_FUNCS > 0) run_call_ret_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_FETCH_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_FETCH_TOTAL_BLOCKS > 0) run_fetch_amplifier_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_PLT_STUB_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_PLT_STUB_FUNCS > 0) run_plt_stub_chain_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_STREAM_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_STREAM_SIZE > 0) run_data_stream_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_INDIRECT_TARGET_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_INDIRECT_TARGET_COUNT > 0) run_indirect_target_set_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_MAIN_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_MAIN_TOTAL_BLOCKS > 0) run_block_loop_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_POINTER_CHASE_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_POINTER_CHASE_PAGE_COUNT > 0) run_data_pointer_chase_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_PAGE_STRIDE_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_PAGE_STRIDE_PAGE_COUNT > 0) run_data_page_stride_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_HOT_L2_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_HOT_L2_SIZE > 0) run_hot_l2_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_INDIRECT_GATHER_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_INDIRECT_GATHER_PAGE_COUNT > 0) run_data_indirect_gather_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_HOT_STRIDE_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_HOT_STRIDE_ACCESS_COUNT > 0) run_data_hot_stride_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_COLD_STRIDE_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_COLD_STRIDE_ACCESS_COUNT > 0) run_data_cold_stride_once();
        }
        for (uint32_t rep = 0; rep < CONFIG_DATA_TLB_INDIRECT_REGION_REPS && !g_abort; ++rep) {
            if (CONFIG_DATA_TLB_INDIRECT_PAGE_COUNT > 0) run_data_tlb_indirect_once();
        }
        ++completed_iters;
    }

    clock_gettime(CLOCK_MONOTONIC, &bench_end);
    double bench_seconds = (double)(bench_end.tv_sec - bench_start.tv_sec) + 1e-9 * (double)(bench_end.tv_nsec - bench_start.tv_nsec);
    printf("completed_iters=%" PRIu64 "\n", completed_iters);
    printf("bench_seconds=%.9f\n", bench_seconds);
    fflush(stdout);
    return g_abort ? 130 : 0;
}
