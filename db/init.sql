CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE SCHEMA content;

CREATE TABLE content.usernames (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE,
    username VARCHAR(255) NOT NULL UNIQUE,
    taken BOOLEAN DEFAULT FALSE
);

INSERT INTO content.usernames (username) VALUES
('shaquille.oatmeal'),
('hanging_with_my_gnomies'),
('hoosier-daddy'),
('fast_and_the_curious'),
('averagestudent'),
('BadKarma'),
('google_was_my_idea'),
('cute_as_ducks'),
('casanova'),
('real_name_hidden'),
('HairyPoppins'),
('fedora_the_explorer'),
('OP_rah'),
('YellowSnowman'),
('Joe_Not_Exotic'),
('username_copied'),
('whos_ur_buddha'),
('unfinished_sentenc'),
('AllGoodNamesRGone'),
('Something'),
('me_for_president'),
('tinfoilhat'),
('oprahwindfury'),
('anonymouse'),
('Definitely_not_an_athlete'),
('HeartTicker'),
('YESIMFUNNY'),
('BenAfleckIsAnOkActor'),
('magicschoolbusdropout'),
('Everybody'),
('regina_phalange'),
('PawneeGoddess'),
('pluralizes_everythings'),
('chickenriceandbeans'),
('test_name_please_ignore'),
('IYELLALOT'),
('heyyou'),
('laugh_till_u_pee'),
('aDistraction'),
('crazy_cat_lady'),
('banana_hammock'),
('thegodfatherpart4'),
('unfriendme'),
('babydoodles'),
('fluffycookie'),
('buh-buh-bacon'),
('ashley_said_what'),
('LactoseTheIntolerant'),
('ManEatsPants'),
('Twentyfourhourpharmacy'),
('applebottomjeans'),
('Babushka'),
('toastedbagelwithcreamcheese'),
('baeconandeggz'),
('FartinLutherKing'),
('coolshirtbra'),
('kentuckycriedfricken'),
('REVERANDTOAST'),
('kim_chi'),
('idrinkchocolatemilk'),
('SaintBroseph'),
('chin_chillin'),
('ghostfacegangsta'),
('bigfootisreal'),
('santas_number1_elf'),
('thehornoftheunicorn'),
('iNeed2p'),
('abductedbyaliens'),
('actuallynotchrishemsworth'),
('nachocheesefries'),
('personallyvictimizedbyreginageorge'),
('just-a-harmless-potato'),
('FrostedCupcake'),
('Avocadorable'),
('fatBatman'),
('quailandduckeggs'),
('PaniniHead'),
('mandymooressingingvoice'),
('catsordogs'),
('FartnRoses'),
('RedMonkeyButt'),
('FreddyMercurysCat'),
('MasterCheif'),
('FreeHugz'),
('ima.robot'),
('actuallythedog'),
('notthetigerking'),
('pixie_dust'),
('ChopSuey'),
('turkey_sandwich'),
('B.Juice'),
('Chris_P_Bacon'),
('LtDansLegs'),
('WookiesrPpl2'),
('hogwartsfailure'),
('CourtesyFlush'),
('MomsSpaghetti'),
('spongebobspineapple'),
('garythesnail'),
('nothisispatrick'),
('CountSwagula'),
('SweetP'),
('PNUT'),
('Snax'),
('Nuggetz'),
('colonel_mustards_rope'),
('baby_bugga_boo'),
('joancrawfordfanclub'),
('fartoolong'),
('loliateyourcat'),
('rawr_means_iloveyou'),
('ihavethingstodo.jpg'),
('heresWonderwall'),
('UFO_believer'),
('ihazquestion'),
('SuperMagnificentExtreme'),
('It_Is_A_Political_Statement'),
('TheAverageForumUser'),
('just_a_teen'),
('OmnipotentBeing'),
('GawdOfROFLS'),
('loveandpoprockz'),
('two_lft_feet'),
('Bread_Pitt'),
('rejectedbachelorcontestant'),
('Schmoople'),
('LOWERCASE_GUY'),
('Unnecessary'),
('joan_of_arks_angel'),
('InstaPrincess'),
('DroolingOnU'),
('Couldnt_Find_Good_Name'),
('AngelWonderland'),
('Born-confused'),
('SargentSaltNPepa'),
('DosentAnyoneCare'),
('quaratineinthesejeans'),
('thanoslefthand'),
('ironmansnap'),
('chalametbmybae'),
('peterparkerspuberty'),
('severusvape'),
('theotherharrypotter'),
('GrangerDanger'),
('BlueIvysAssistant'),
('Ariana_Grandes_Ponytail'),
('HotButteryPopcorn'),
('MelonSmasher'),
('morgan_freeman_but_not'),
('potatoxchipz'),
('FoxtrotTangoLove'),
('ElfishPresley'),
('WustacheMax'),
('JuliusSeizure'),
('HeyYouNotYouYou'),
('OneTonSoup'),
('HoneyLemon'),
('LoveMeKnot'),
('Bud_Lightyear'),
('takenbyWine'),
('taking0ver'),
('Unic0rns'),
('in_jail_out_soon'),
('hotgirlbummer'),
('behind_you'),
('itchy_and_scratchy'),
('not_james_bond'),
('a_collection_of_cells'),
('CowabungaDude'),
('TeaBaggins'),
('bill_nye_the_russian_spy'),
('intelligent_zombie'),
('imma_rage_quit'),
('kiss-my-axe'),
('king_0f_dairy_queen'),
('desperate_enuf'),
('AirisWindy'),
('cheeseinabag'),
('MakunaHatata'),
('rambo_was_real'),
('churros4eva'),
('namenotimportant'),
('i_boop_ur_nose'),
('image_not_uploaded'),
('suck_my_popsicle'),
('sofa_king_cool'),
('RootinTootinPutin'),
('blousesandhouses'),
('iblamejordan'),
('manic_pixie_meme_girl'),
('Technophyle'),
('Cuddly-Wuddly'),
('JesusoChristo'),
('peap0ds'),
('whats_ur_sign'),
('TheMilkyWeigh'),
('BabyBluez'),
('BarbieBreath'),
('MangoGoGo'),
('DirtBag'),
('FurReal'),
('ScoobyCute'),
('YouIntradouchingMyshelf'),
('IwasReloading'),
('WellEndowedPenguin'),
('TheAfterLife'),
('PuppiesnKittens'),
('WakeAwake'),
('Coronacosmo'),
('wherearetheavocados'),
('ijustwanttobeme'),
('TheKidsCallMeBoss'),
('SewerSquirrel'),
('because.i.like.to.like'),
('notmuchtoit'),
('friedchocolate'),
('DonWorryItsGonBK'),
('Early_Morning_Coffee'),
('drunkbetch'),
('strawberry_pineapple'),
('MissPiggysDimples'),
('chickenbaconranchpizza'),
('cereal_killer'),
('khaleesisfourthdragon'),
('darth.daenerys'),
('LeslieKnopesBinder'),
('BettyBoopsBoop'),
('Freddie_Not_The_Fish'),
('Billys_Mullet'),
('Calzone_Zone'),
('ChickyChickyParmParm'),
('Adobo_Ahai'),
('theoldRazzleDazzle'),
('Not-Insync'),
('Toiletpaperman'),
('Reese_WitherFork'),
('LizzosFlute'),
('Macauliflower_Culkin'),
('Llama_del_Rey'),
('Hot_Name_Here'),
('Carmelpoptart'),
('notfunnyatall'),
('Mangonificent'),
('toastcrunch'),
('fizzysodas'),
('kokonuts'),
('cherry-picked');