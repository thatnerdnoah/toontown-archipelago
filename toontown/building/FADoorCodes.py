from toontown.toonbase import TTLocalizer, ToontownGlobals

UNLOCKED = 0
TALK_TO_TOM = 1
DEFEAT_FLUNKY_HQ = 2
TALK_TO_HQ = 3
WRONG_DOOR_HQ = 4
GO_TO_PLAYGROUND = 5
DEFEAT_FLUNKY_TOM = 6
TALK_TO_HQ_TOM = 7
SUIT_APPROACHING = 8
BUILDING_TAKEOVER = 9
SB_DISGUISE_INCOMPLETE = 10
CB_DISGUISE_INCOMPLETE = 11
LB_DISGUISE_INCOMPLETE = 12
BB_DISGUISE_INCOMPLETE = 13

# Archipelago Locks
TTC_ACCESS_MISSING = 14
DD_ACCESS_MISSING = 15
DG_ACCESS_MISSING = 16
MM_ACCESS_MISSING = 17
TB_ACCESS_MISSING = 18
DDL_ACCESS_MISSING = 19

FRONT_FACTORY_ACCESS_MISSING = 20
SIDE_FACTORY_ACCESS_MISSING = 21

COIN_MINT_ACCESS_MISSING = 22
DOLLAR_MINT_ACCESS_MISSING = 23
BULLION_MINT_ACCESS_MISSING = 24

OFFICE_A_ACCESS_MISSING = 25
OFFICE_B_ACCESS_MISSING = 26
OFFICE_C_ACCESS_MISSING = 27
OFFICE_D_ACCESS_MISSING = 28

FRONT_THREE_ACCESS_MISSING = 29
MIDDLE_SIX_ACCESS_MISSING = 30
BACK_NINE_ACCESS_MISSING = 31

TTC_FISHING_MISSING = 32
DD_FISHING_MISSING = 33
DG_FISHING_MISSING = 34
MM_FISHING_MISSING = 35
TB_FISHING_MISSING = 36
DDL_FISHING_MISSING = 37

ZONE_TO_ACCESS_CODE = {
    ToontownGlobals.ToontownCentral: TTC_ACCESS_MISSING,
    ToontownGlobals.DonaldsDock: DD_ACCESS_MISSING,
    ToontownGlobals.DaisyGardens: DG_ACCESS_MISSING,
    ToontownGlobals.MinniesMelodyland: MM_ACCESS_MISSING,
    ToontownGlobals.TheBrrrgh: TB_ACCESS_MISSING,
    ToontownGlobals.DonaldsDreamland: DDL_ACCESS_MISSING,
}

LICENSE_TO_ACCESS_CODE = {
    ToontownGlobals.ToontownCentral: TTC_FISHING_MISSING,
    ToontownGlobals.DonaldsDock: DD_FISHING_MISSING,
    ToontownGlobals.DaisyGardens: DG_FISHING_MISSING,
    ToontownGlobals.MinniesMelodyland: MM_FISHING_MISSING,
    ToontownGlobals.TheBrrrgh: TB_FISHING_MISSING,
    ToontownGlobals.DonaldsDreamland: DDL_FISHING_MISSING,
}

FACILITY_TO_ACCESS_CODE = {
    ToontownGlobals.SellbotFactoryInt: FRONT_FACTORY_ACCESS_MISSING,
    ToontownGlobals.SellbotFactoryIntS: SIDE_FACTORY_ACCESS_MISSING,

    ToontownGlobals.CashbotMintIntA: COIN_MINT_ACCESS_MISSING,
    ToontownGlobals.CashbotMintIntB: DOLLAR_MINT_ACCESS_MISSING,
    ToontownGlobals.CashbotMintIntC: BULLION_MINT_ACCESS_MISSING,

    ToontownGlobals.LawbotStageIntA: OFFICE_A_ACCESS_MISSING,
    ToontownGlobals.LawbotStageIntB: OFFICE_B_ACCESS_MISSING,
    ToontownGlobals.LawbotStageIntC: OFFICE_C_ACCESS_MISSING,
    ToontownGlobals.LawbotStageIntD: OFFICE_D_ACCESS_MISSING,

    ToontownGlobals.BossbotCountryClubIntA: FRONT_THREE_ACCESS_MISSING,
    ToontownGlobals.BossbotCountryClubIntB: MIDDLE_SIX_ACCESS_MISSING,
    ToontownGlobals.BossbotCountryClubIntC: BACK_NINE_ACCESS_MISSING,
}

reasonDict = {
    UNLOCKED: TTLocalizer.FADoorCodes_UNLOCKED,
    TALK_TO_TOM: TTLocalizer.FADoorCodes_TALK_TO_TOM,
    DEFEAT_FLUNKY_HQ: TTLocalizer.FADoorCodes_DEFEAT_FLUNKY_HQ,
    TALK_TO_HQ: TTLocalizer.FADoorCodes_TALK_TO_HQ,
    WRONG_DOOR_HQ: TTLocalizer.FADoorCodes_WRONG_DOOR_HQ,
    GO_TO_PLAYGROUND: TTLocalizer.FADoorCodes_GO_TO_PLAYGROUND,
    DEFEAT_FLUNKY_TOM: TTLocalizer.FADoorCodes_DEFEAT_FLUNKY_TOM,
    TALK_TO_HQ_TOM: TTLocalizer.FADoorCodes_TALK_TO_HQ_TOM,
    SUIT_APPROACHING: TTLocalizer.FADoorCodes_SUIT_APPROACHING,
    BUILDING_TAKEOVER: TTLocalizer.FADoorCodes_BUILDING_TAKEOVER,
    SB_DISGUISE_INCOMPLETE: TTLocalizer.FADoorCodes_SB_DISGUISE_INCOMPLETE,
    CB_DISGUISE_INCOMPLETE: TTLocalizer.FADoorCodes_CB_DISGUISE_INCOMPLETE,
    LB_DISGUISE_INCOMPLETE: TTLocalizer.FADoorCodes_LB_DISGUISE_INCOMPLETE,
    BB_DISGUISE_INCOMPLETE: TTLocalizer.FADoorCodes_BB_DISGUISE_INCOMPLETE,
    TTC_ACCESS_MISSING: TTLocalizer.FADoorCodes_TTC_ACCESS_MISSING,
    DD_ACCESS_MISSING: TTLocalizer.FADoorCodes_DD_ACCESS_MISSING,
    DG_ACCESS_MISSING: TTLocalizer.FADoorCodes_DG_ACCESS_MISSING,
    MM_ACCESS_MISSING: TTLocalizer.FADoorCodes_MM_ACCESS_MISSING,
    TB_ACCESS_MISSING: TTLocalizer.FADoorCodes_TB_ACCESS_MISSING,
    DDL_ACCESS_MISSING: TTLocalizer.FADoorCodes_DDL_ACCESS_MISSING,

    FRONT_FACTORY_ACCESS_MISSING: TTLocalizer.FADoorCodes_FRONT_FACTORY_ACCESS_MISSING,
    SIDE_FACTORY_ACCESS_MISSING: TTLocalizer.FADoorCodes_SIDE_FACTORY_ACCESS_MISSING,

    COIN_MINT_ACCESS_MISSING: TTLocalizer.FADoorCodes_COIN_MINT_ACCESS_MISSING,
    DOLLAR_MINT_ACCESS_MISSING: TTLocalizer.FADoorCodes_DOLLAR_MINT_ACCESS_MISSING,
    BULLION_MINT_ACCESS_MISSING: TTLocalizer.FADoorCodes_BULLION_MINT_ACCESS_MISSING,

    OFFICE_A_ACCESS_MISSING: TTLocalizer.FADoorCodes_OFFICE_A_ACCESS_MISSING,
    OFFICE_B_ACCESS_MISSING: TTLocalizer.FADoorCodes_OFFICE_B_ACCESS_MISSING,
    OFFICE_C_ACCESS_MISSING: TTLocalizer.FADoorCodes_OFFICE_C_ACCESS_MISSING,
    OFFICE_D_ACCESS_MISSING: TTLocalizer.FADoorCodes_OFFICE_D_ACCESS_MISSING,

    FRONT_THREE_ACCESS_MISSING: TTLocalizer.FADoorCodes_FRONT_THREE_ACCESS_MISSING,
    MIDDLE_SIX_ACCESS_MISSING: TTLocalizer.FADoorCodes_MIDDLE_SIX_ACCESS_MISSING,
    BACK_NINE_ACCESS_MISSING: TTLocalizer.FADoorCodes_BACK_NINE_ACCESS_MISSING,

    TTC_FISHING_MISSING: TTLocalizer.FADoorCodes_TTC_FISHING_MISSING,
    DD_FISHING_MISSING: TTLocalizer.FADoorCodes_DD_FISHING_MISSING,
    DG_FISHING_MISSING: TTLocalizer.FADoorCodes_DG_FISHING_MISSING,
    MM_FISHING_MISSING: TTLocalizer.FADoorCodes_MM_FISHING_MISSING,
    TB_FISHING_MISSING: TTLocalizer.FADoorCodes_TB_FISHING_MISSING,
    DDL_FISHING_MISSING: TTLocalizer.FADoorCodes_DDL_FISHING_MISSING,
}
