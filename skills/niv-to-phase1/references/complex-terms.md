# Complex Term Handling — Pairing & Explication Lookup

Source: the project's "05 How to handle Complex Terms.xlsx" reference file, exported here as a static table so it does not need to be re-opened or looked up live for every word. This is the detailed guidance rule 0.2 (`references/phase1-rules.md`) points to, and it is the primary companion document the skill was previously missing.

**How to use this file:** for any content word, check here first. If the word appears below with a `Paired with` or `Explication` value, use that directly — it has already been checked against the ontology, so it saves a live `/simplification_hints` call. If the word is not listed here at all, or is listed with no guidance recorded, fall back to the live ontology endpoints (`SKILL.md` step 5) — this table is a large but not exhaustive snapshot, and the live ontology is always the source of truth if the two ever disagree.

Column meanings: **Level** is the ontology complexity level at the time this file was compiled (0/1 = usable bare; 2/3 = needs a pairing/explication/complex-alternate per rule 0.2; 4 = proper-noun-like; `n/a` = not an ontology entry at all). **Paired with** is the simple word for `simple/complex` notation (rule 0.2) — write the simple word first. **Explication** is a bracketed-phrase substitute to use instead of a pairing. **Structure** notes the word's argument pattern where relevant (mostly verbs/verbal phrases). A row can have both a pairing and an explication recorded; either is valid — pick whichever reads better in context (rule 0.30 — must work on either side).

**1469 total entries.** By status: in ontology (834), not used (354), approved (274), suggested (6), (blank) (1). By level: level 2 (981), n/a (354), level 1 (81), level 3 (46), level 4 (6), (blank) (1).

## In ontology — recognized, level and (where recorded) pairing/explication confirmed

834 entries. Status `in ontology` means the term itself is a real ontology entry at the given level — for level 2/3 terms, use the recorded pairing/explication; a blank Paired-with/Explication means no guidance was recorded in this sheet yet even though the term and level are confirmed, so check `/simplification_hints` live for those.

| Term | POS | Level | Paired with | Explication | Structure | Notes |
|---|---|---|---|---|---|---|
| abandon-A | Verb | level 2 |  |  |  |  |
| abundant-A | Adjective | level 2 | much-many |  |  |  |
| abundantly-A | Adverb | level 2 | much |  |  | Do we need this? |
| accomplish-A | Verb | level 2 | do |  |  |  |
| accuse-A | Verb | level 2 |  | "say-C [X did bad-B things]" | accuse X |  |
| accuse-A | Verb | level 2 |  | Use "say-C/accuse [X did Y]" | accuse X [of doing Y] |  |
| accuse-B | Verb | level 2 | oppose |  | accuse X |  |
| acknowledge-A | Verb | level 2 |  |  | acknowledge X |  |
| adultery-A | Noun | level 2 |  | New: “X sexes a man//woman//person [that X is not married to]” Or use “X sexes a man//woman//person [who is not the husband//wife of X]”, or with “husband or wife” if the sex of the person is not known. For the case of remarriage, use "is not faithful to X's previous husband//wife". “Spouse” can be paired with husband or wife if desired, but probably the more specific term is better. | do/commit adultery |  |
| adultery-A | Noun | level 2 |  | “X sexes Y [who is not the husband//wife of X]” | do/commit adultery with Y |  |
| adviser-A | Noun | level 2 |  | "person _mustBe3rdPerson [who advises people _generic]" |  |  |
| alabaster-A | Noun | level 2 |  | “beautiful white and yellow stone” |  |  |
| alert-A | Adjective | level 2 |  | “be//become able _AorB [to think quickly and clearly]” | be//become alert |  |
| aloe-A | Noun | level 2 | oil | Note: In Proverbs, I paired with nothing |  |  |
| altar-A | Noun | level 2 |  | Generic: “structure [that people give gifts//sacrifices to God//Yahweh on]”. Also, “structure [that people give gifts//sacrifices on]” without a destination argument. For "sacrifices", use "gifts/sacrifices". |  |  |
| altar-A | Noun | level 2 |  | “structure of God//Yahweh _optionalButImplied [that people give gifts/sacrifices to God//Yahweh on]” | altar of God//Yahweh |  |
| altar-A | Noun | level 2 |  | “structure [that people give gifts/sacrifices to X on]” | altar of X (not God or Yahweh) |  |
| amaze-A | Verb | level 2 | surprise//confuse |  |  |  |
| amazed-A | Adjective | level 2 | surprised | Note: a theta grid for English changes “very amazed” to just “amazed” | X is amazed |  |
| amazed-B | Adjective | level 2 | surprised |  | X is amazed by Y |  |
| ambush-A | Verb | level 2 | attack-C//fight |  |  |  |
| ancestor-A | Noun | level 2 | Person or father | Suggestion: use explicit pairing, “person/ancestor”, or “father/ancestor” or “parent/ancestor”, depending on the context |  |  |
| anchor-A | Noun | level 2 |  | Suggestion: “ heavy object [ that causes a ship to move slower]” or “ to stop moving” |  |  |
| angel-A | Noun | level 2 |  | “servent//servant/messenger [who comes from God]” - the rule should work with either servant or messenger |  |  |
| angel-A | Noun | level 2 |  | “messenger of God//Lord-A//Yahweh” - use “servant/messenger in the phase 1” | angel of God//Lord-A//Yahweh |  |
| announce-A | Verb | level 2 | say |  | X announced [" "} |  |
| announce-B | Verb | level 2 | say |  | X announced [that... ] |  |
| announce-C | Verb | level 2 | tell |  | X announced Y |  |
| anoint-A | Verb | level 2 | choose//fill(for with Holy Spirit) | “Put oil on Y” Alternate rule for burial: “put spices on Y” or pair with “choose”. Consider "fill/anoint with Holy Spirit" for anointing with Holy Spirit | X anoint Y |  |
| anoint-B | Verb | level 2 |  | "X put oil on Y [so that Y could//would do something]" | X anoint Y [to Z] |  |
| apostle-A | Noun | level 3 | Or pair with leader//representative//etc | New explication: "a//the//that person//man//leader [that Jesus//Christ//God//Holy-Spirit sent to people _genericOptional [so that a//the//that person//man would be for people _genericOptional Christ's/Jesus's representative]]". After using the explication, you can pair with “representative” or “leader” or “Jesus’s//Christ’s(possibly implicit) representatives//leaders”. People have been using “men” in Acts for the 12 apostles, and I suggest that we continue doing that normally. [] The older explication, which should also work, is: "a//the//that person//man [that Jesus//Christ//Christ Jesus sent [so that a//the//that person//man would tell//teach/preach God's message//Good-News to people]]", followed by the pairing with “person//man”. [] For "apostle of Jesus//Christ",  use "representative/apostle of Jesus//Christ". Previously we talked about pairing with “leader”. That might work in some circumstances, but doesn’t work well with the explications. You can also use a complex alternate (if necessary) |  |  |
| appoint-A | Verb | level 2 | choose |  |  |  |
| approach-A | Verb | level 2 | come |  |  |  |
| ark-A | Noun | level 2 |  | “big boat”, optionally with “[that (implicit-situational) God told [Noah to build]]” (we don’t like “big boat”, but don’t have a better idea right now) |  |  |
| armor-A | Noun | level 2 |  | "hard clothes" or "clothes [that protect X]" |  |  |
| arrest-A | Verb | level 2 | take-away |  |  |  |
| arrogant-A | Adjective | level 2 | rude//proud |  |  |  |
| arrow-A | Noun | level 2 | weapon | “stick-B [that has a sharp point]” | arrow |  |
| arrow-A | Noun | level 2 |  | “stick-B [that has a very sharp point]” | sharp arrow |  |
| ash-A | Noun | level 2 |  | ashes of X = dust _usuallyPlural [that stay [after X burns]] ashes = dust [that stay [after thing-A burns]] |  |  |
| assist-A | Verb | level 2 | help |  |  |  |
| astrologer-A | Noun | level 2 |  | "person [who searches signs-B [that are in the sky-B]]" |  | (though only used 9 times) |
| axe-A | Noun | level 2 |  | Suggestion: As a generic explication, "tool [that has a big sharp blade] [(implicit-background) and that people use [in order to cut wood]]". But consider pairing with "tool" or "object" or "sword" or “weapon” (if it's used as a weapon). |  |  |
| bamboo-A | Noun | level 2 | wood-B (the material) |  |  | (though not in the Bible) |
| bandage-A | Noun | level 2 | cloth-A |  |  |  |
| bank-B | Noun | level 2 | side//shore |  |  |  |
| baptize-A | Verb | level 2 |  | Use “dip X in(destination) the water of Y” | baptize X in Y |  |
| baptize-A | Verb | level 2 |  | Use “dip X in(destination) water”. For "baptized in water", use "dip/ baptize in water" | baptize X |  |
| baptize-B | Verb | level 2 |  | Use “unite/baptize _baptizeB X to(destination) Y”. A theta grid rule should change “baptize to” to “baptize into”. (Previously we used “wash/baptize”, but we do not now prefer this, so “wash/baptize” will need to be changed.)bee | baptize X into Y |  |
| bark-A | Noun | level 2 | cover | “part of a tree [that covers that tree]” |  | it’s in the ontology now, but only used 2 times in the Bible |
| barley-A | Noun | level 2 | crop//grain |  |  |  |
| barley-B | Noun | level 2 | grain |  |  |  |
| barn-A | Noun | level 2 |  | “big farm building” |  |  |
| barren-A | Adjective | level 2 | empty//dry |  |  |  |
| battlefield-A | Noun | level 2 |  | "place//field of battle" ("field" only if it's really a field) |  |  |
| be-fulfilled-A | Verb | level 2 | happen |  |  |  |
| beam-A | Noun | level 2 | pole |  |  |  |
| beast-A | Noun | level 2 |  | "a big and dangerous wild animal" |  |  |
| beauty-A | Noun | level 3 |  | supply a simple alternate |  |  |
| bedroom-A | Noun | level 2 |  | "room [that person sleeps in]" |  |  |
| bedroom-A | Noun | level 2 |  | "room [that X(not person) sleeps in]" | X's bedroom |  |
| bee-A | Noun | level 2 | insect |  |  |  |
| beg-A | Verb | level 2 | ask//tell |  | beg X [to Y] |  |
| beg-B | Verb | level 2 |  | “X asks [people to give money//food//bread//things to X [so that X could live]]”. |  |  |
| beg-C | Verb | level 2 | ask (for question) say or tell (for statement) |  | beg [" "] |  |
| beginning-A | Noun | level 3 |  |  |  |  |
| behold-A | Verb | level 2 | look//listen |  |  |  |
| believer-A | Noun | level 2 |  | Use: “Person//man//woman _require3rdPerson [who believes in Jesus//God]” or “person//man//woman  _require3rdPerson [who believes in Jesus Christ _blockChristian]” Or consider pairing with something like “person” or “follower”. [] Note: We used to allow just “Christ”, but that leads to a conflict with “Christian” |  |  |
| bend-over-A | Verb | level 2 | kneel//stand | OR ‘bend X’s body toward the ground’ |  |  |
| berry-A | Noun | level 2 | fruit (which may be plural even  though it is a mass noun in English) |  |  |  |
| besiege-A | Verb | level 2 | surround//attack |  |  |  |
| betray-A | Verb | level 2 |  | “give Y to Y’s enemies”; or you can pair with give, take, bring, talk about, or deceive | X betrays Y |  |
| betray-A | Verb | level 2 | give//take | if Z is not "Y's enemies" | X betrays Y to Z |  |
| betray-B | Verb | level 2 |  | "treat friend badly", or "treat "Y [who is X's friend] badly", or "treat Y badly [even-though Y is X's friend]" | X betrays Y |  |
| bind-A | Verb | level 2 |  |  | tie-C |  |
| birth-A | Noun | level 1 |  | Suggestion: use the verb "birth" |  |  |
| birthday-A | Noun | level 2 |  | "day [that X was born on] of the year" | X's birthday |  |
| bitter-B | Adjective | level 2 | sad//angry//upset |  |  |  |
| blameless-A | Adjective | level 2 | good-B |  |  |  |
| blaspheme-A | Verb | level 2 |  | “much insult God//Holy-Spirit//Jesus//Lord-B//Lord-A//Christ//Moses” or "name of God//Holy-Spirit//Jesus//Lord-B//Lord-A//Christ//Moses" in the explication . Or in some cases, something like “talk [just-like X is God]”? | blaspheme God//Holy-Spirit//Lord-A//Christ//Moses |  |
| bleach-A | Noun | level 2 |  | "substance [that causes [cloth//clothes to become white]]" or "substance [that kills extremely small creatures [that cause [people to have diseases]]" |  |  |
| bless-A | Verb | level 2 |  | “X says//prays [good-A things will happen to Y]” | X blesses Y |  |
| bless-B | Verb | level 2 |  | “God//Yahweh//Jesus does good-A things for X” or “God//Yahweh//Jesus does many good-A things for X”; Use "much did..." for "greatly blesses" | God//Yahweh blesses X |  |
| blessed-A | Adjective | level 2 |  | Use in a complex alternate or in some circumstances (but see below),  it might be possible to pair with a word like "happy".  or here are suggestions for a simple alternate: Use the verb form "bless". We could consider it with "happy" (good news version for the Beatitudes) or "fortunate" (in the LDV). (Tod doesn’t like “fortunate” and TN recommends against “happy”, so it’s probably best to use the verb form for the Beattitudes.) |  |  |
| blessing-A | Noun | level 2 |  | Use in a complex alternate, or possibly you could pair with “things-B” or "things-D" or“actions” or "gifts". Otherwise, I suggest you use something like “do good things for” = “bless _verb”. if you do a complex alternate, you will need a simple alternate doing something like this. |  |  |
| blind-A | Adjective | level 2 |  | “person//man//woman//child//girl//boy [who is not able [to see {things-A _generic}_OptionalInExplication]]” | blind X |  |
| blind-A | Adjective | level 2 |  | “is not able [to see things-B _genericIfIncludedButArgumentOptional]”. Note: The rule for “blind X” needs to be checked first (Currently “things” is required, but it shouldn’t be.) | be blind |  |
| blind-A | Adjective | level 2 |  | “always not be able [to see things _genericOptional]”. Note: The rule for “blind X” needs to be checked first (Currently “things” is required, but it shouldn’t be.) | Always be Blind |  |
| blot-out-A | Verb | level 2 | cover//hide//take-away |  |  |  |
| boast-A | Verb | level 2 |  | “talk//speak proudly-A about Y _optional” | X boast about Y _optional |  |
| boast-B | Verb | level 2 |  | "proudly-A say that ..."  with indirect quote | X boast [... ] |  |
| boast-C | Verb | level 2 |  | talk//speak proudly-B about Y _optional | X boasts about Y _optional |  |
| boil-A | Noun | level 2 |  | "infected sore that has pus". Previously "a red place [that is on X's skin] [and that hurts-B]", but that is complicated and sounds like the definition of "sore". Or pair with "sore" |  |  |
| bold-A | Adjective | level 2 | brave |  |  |  |
| boldly-A | Adverb | level 2 | bravely |  |  |  |
| boss-A | Noun | level 2 | leader//master |  |  |  |
| both-A | Adjective | level 1 |  | We do not use "both X and Y". We only use "both" with a dual noun, like "both men _dual". | both X and Y |  |
| bother-A | Verb | level 2 | annoy |  |  |  |
| bow-A | Verb | level 2 | kneel |  |  |  |
| bow-A | Noun | level 2 |  | "weapon [that X uses [in order to shoot arrows]]" - use explication for arrows |  |  |
| bracelet-A | Noun | level 2 |  | "jewelry [that is on X's arm//wrist]" or pair with "jewelry" ("wrist" is in the LDV, so we can add it as a simple word if you want it) |  |  |
| breast-milk-A | Noun | level 2 |  | "milk [that comes from a woman's//mother's _notRoutine breast]" (Note: if the noun is not routine, it won't refer back to someone who's already been mentioned) |  |  |
| breast-milk-A | Noun | level 2 |  | "milk [that comes from X's breast]" which can work with "woman" or "mother" also as long as they are routine | X's breast-milk |  |
| breastplate-A | Noun | level 2 |  | Use “piece of metal [that covers X’s chest]” |  |  |
| bribe-A | Noun | level 2 |  | “money [that a person gives to a person [in order to cause [a person to do a bad-B thing-B]]]” You might want to block rules for “sin”. |  |  |
| bribe-A | Noun | level 2 |  | “gives money to X [in order to cause [X to do a bad-B thing-B]]”. Note: check “Bribe” rule first. You might want to block rules for “sin”. | give a bribe to X |  |
| bride-A | Noun | level 2 | woman | “woman [who will marry a man//bridegroom soon_optional]” For different verb tense or different participant tracking (the or that woman//bridegroom), use the explication |  |  |
| bridegroom-A | Noun | level 2 |  | Current explication: “man [who is marrying a woman//bride soon_optional]” For different verb tense or different participant tracking (the or that woman//bride), use the explication |  |  |
| bridle-A | Noun | level 2 |  | "A piece [that a person puts into the mouth of a horse [in order to control a horse]] of leather or of metal", or in one case we are using "height of horses neck/bridle"" |  |  |
| brightly-A | Adverb | level 2 | much |  |  |  |
| bronze-A | Noun | level 2 | metal |  |  |  |
| brother-D | Noun | level 2 | Friend//people | Suggestion: Use the complex pairing suggested. For “brothers and sisters”, you could use “friends/brothers-D and null/sisters-D _implicit”, then it will just come out “friends” if the complex terms are not allowed |  |  |
| brother-in-law-A | Noun | level 2 |  | "brother of X's wife//husband//spouse" ("spouse" is complex - see how to represent it by looking at the entry for "spouse") | X's brother-in-law |  |
| bucket-A | Noun | level 2 | container | Bucket is in the LDV, but if it remains complex: “a container [that a person uses [in order to get/draw water]]” |  | make it simple? |
| bull-A | Noun | level 2 |  | “male cow” or pair with “cow” |  |  |
| butter-A | Noun | level 1 |  | "solid food [that is made-E by X _optionallyImplicit from milk _addSourceArgument]" |  |  |
| cage-A | Noun | level 2 |  | "structure of _madeOf bars//sticks-B//boards-B [that prevents [X from escaping]]" |  |  |
| calf-A | Noun | level 2 |  | “a young//baby cow” |  |  |
| camel-A | Noun | level 2 |  | “big desert animal”, or “big animal of the desert that is able to carry people”, or in most cases you can pair with “animal” |  |  |
| cancel-A | Verb | level 2 | end-C |  |  |  |
| candle-A | Noun | level 2 | lamp |  |  |  |
| captain-A | Noun | level 2 | leader |  |  |  |
| capture-A | Verb | level 2 | catch//defeat |  |  |  |
| capture-B | Verb | level 2 | take-D//defeat |  |  |  |
| carpenter-A | Noun | level 2 |  | “person [who builds things with wood]” |  | it’s already in the ontology, though not used enough times to make it worthwhile |
| castanet-A | Noun | level 2 | instrument |  |  |  |
| cave-A | Noun | level 2 | hole |  |  |  |
| cedar-A | Noun | level 2 | the new "wood-B", which will mean the material |  |  |  |
| cemetery-A | Noun | level 2 |  | “place [where people bury _routinely people]” |  |  |
| centurion-A | Noun | level 2 |  | “Roman officer [who commanded about 100 soldiers]” Before had “Roman//military officer [who commanded about 100 soldiers]” |  |  |
| chaff-A | Noun | level 2 |  | “covers of grain” (Genevieve. Hartmut Wiens suggested for Matt. 3.12) |  |  |
| chariot-A | Noun | level 2 |  | “vehicle/wagon of war” *please note this has been adjusted from "war vehicle/wagon". This order is better for the P2 |  |  |
| chasm-A | Noun | level 2 |  | "valley [that has steep sides]" or pair with "valley" |  |  |
| cherub-A | Noun | level 2 |  | "servant [that has wings] of God" |  |  |
| chief-A | Noun | level 2 | leader |  |  |  |
| choir-A | Noun | level 2 |  | "group of people [who sing]" |  |  |
| choke-A | Verb | level 2 |  | “squeeze X’s throat”, or pair with "kill" or "hurt" or "press against" or "squeeze" | choke X |  |
| Christian-A | Noun | level 2 |  | “person [who believes in Christ]” (The old explication: “person [who believes in//trusts Jesus//Christ]”, needs to be replaced because of a conflict with “believer”) |  |  |
| church-A | Noun | level 2 |  | Write “group of people [that believe in Christ//Jesus//Christ Jesus]” (=”group of believers// Christians”) |  |  |
| church-B | Noun | level 2 |  | Write "building [that people [who believe in Christ] worship God in]". Note that “people [who believe in Christ]= Christians”). Alternate rule: "building [that people [who believe in Christ] meet in". |  |  |
| cinnamon-A | Noun | level 2 | Spice |  |  |  |
| circumcise-A | Verb | level 2 |  | “cut off the skin [that is at the end of X’s penis]” Note: for plural people use "skin _plural" and "penises" | circumcise X |  |
| circumcised-A | Adjective | level 2 |  | “X does not have skin on the end of X’s penis [because skin was cut-off by a person _optionallyImplicitActiveAgent]” Note: for plural people use "skin _plural" , "penises", and "by people" (Note: We used to have “the skin [that was at the end of X’s penis] was cut off by a person _ optionallyImplicitActiveAgent”, but that is the same as the explication for the verb "circumcise".) | be circumcised |  |
| circumcised-A | Adjective | level 2 |  | “X has skin [that was not cut off by a person _ optionallyImplicitActiveAgent] on the end of X’s penis” Note: for plural people use "skin _plural" , "penises", and "by people" | not be circumcised |  |
| circumcised-A | Adjective | level 2 |  | “Allow [a person to cut off the skin [that was at the end of X’s penis]]”. Note: for plural people use "skin _plural" , "penises", and "by people"  Suggestion: If you want it to use priest, use the explicit explication | Become-circumcised |  |
| cistern-A | Noun | level 2 |  | big container of water |  |  |
| citizen-A | Noun | level 2 | person | Example: “This man is a Roman person/citizen” |  |  |
| claim-A | Verb | level 2 | Say or think |  |  |  |
| clan-A | Noun | level 2 | family | ‘group of families’, or pair with family |  |  |
| clean-B | Adjective | level 2 |  | “religiously clean-A” |  |  |
| cliff-A | Noun | level 2 |  | "steep side of land//rock//mountain" |  |  |
| clinic-A | Noun | level 2 |  | “building [where a doctor treats people [who were sick]]”, or pair with “building”. (Could add “nurse” for explication.) |  |  |
| club-A | Noun | level 2 |  | “short heavy stick” |  |  |
| coast-A | Noun | level 2 | shore |  |  |  |
| coffin-A | Noun | level 2 |  | “box [that a dead X is/will be in]” |  |  |
| cold-A | Noun | level 2 | disease |  |  |  |
| colt-A | Noun | level 2 |  | "young horse//donkey" |  |  |
| comb-A | Noun | level 2 |  | "flesh [that is on the head] of bright colors" | (of a rooster) |  |
| comb-A | Verb | level 1 |  | "small thing//tool [that people use [in order to cause [people's hair to be flat]]]" or pair with "tool" |  |  |
| commander-A | Noun | level 2 |  | "military leader"; you can also pair with leader |  |  |
| commandment-A | Noun | level 2 | Command (or we might want to make this level 1 because of its very frequent use) |  |  |  |
| companion-A | Noun | level 2 | friend//person// |  |  |  |
| compassion-A | Noun | level 2 | love | but consider using 'kind//merciful' |  |  |
| concern-A | Verb | level 2 | care-B//worry |  | to be concerned about |  |
| concubine-A | Noun | level 2 |  | “other woman [that a man sexes]”. Or if you want to change “a man” use the explicit explication. Or pair with “woman” or “wife” |  |  |
| condemn-A | Verb | level 2 |  | “to decide [to punish//destroy X]". Must be “punish//destroy” in the affirmative. Or you can pair it with “punish//destroy”. |  |  |
| condemn-B | Verb | level 2 |  | "decide [X is bad-B//guilty]" or "decide [X should be punished by God _implicitActiveAgent]", or pair with "judge" | condemn X |  |
| condom-A | Noun | level 2 |  | "thing [that covers the penis]" |  |  |
| confess-A | Verb | level 2 | admit-B | Note: this is for admitting sin, not for "confessing Christ", for which you should use "acknowledge that ..." | X confesses Y to Z |  |
| confess-B | Verb | level 2 | admit-A |  | X confesses [that... ] |  |
| conquer-A | Verb | level 2 | defeat |  |  |  |
| conscience-A | Noun | level 2 | mind |  |  |  |
| consecrate-A | Verb | level 2 | give |  |  |  |
| conspire-A | Verb | level 2 | plan |  |  |  |
| copper-A | Noun | level 2 | metal |  |  |  |
| cornerstone-A | Noun | level 2 |  | “the chief stone of the corner of a building _optionallyImplicitOrOmitted” (with the optional or implicit “building” recommended but not required for the rule) |  |  |
| corpse-A | Noun | level 2 | body-A | Note that previously we said to use the explication "dead body", but "body-A" means a dead body, so adding "dead" is redundant. We might consider getting rid of "corpse" in the future, since that's what "body-A" means. |  |  |
| correct-A | Verb | level 2 |  | “tell//teach//instruct X about the bad-B//bad-A things [that X did]” |  |  |
| corrupt-A | Adjective | level 2 | bad-B |  |  |  |
| couch-A | Noun | level 2 | seat |  |  |  |
| courageous-A | Adjective | level 2 | brave |  |  |  |
| courtyard-A | Noun | level 2 | yard (if P2 approves adding that sense), otherwise area or space |  |  |  |
| cousin-A | Noun | level 2 |  | “the child//son//daughter of the brother//sister of X’s parent//father//mother”. Or pair with “relative” | X's cousin |  |
| covenant-A | Noun | level 2 |  | "special agreement". Or pair with "agreement" or "promise". |  |  |
| covet-A | Verb | level 2 | want |  |  |  |
| crawl-A | Verb | level 2 |  | "X goes//moves on X's hands and X's knees" | X crawls |  |
| create-A | Verb | level 2 | make | Note: Our current sense means “create from nothing” |  |  |
| criminal-A | Noun | level 2 |  | “person [who breaks laws]” |  |  |
| crippled-A | Adjective | level 2 |  | Suggestion: “person [who has a part of that person’s body [that was damaged by a thing-B _implicitActiveAgent]] | crippled X or X is crippled |  |
| criticize-A | Verb | level 2 |  | “talk about the bad-A//bad-B characteristics of X” | criticize X |  |
| crowd-A | Verb | level 2 | surround |  | crowds around |  |
| crown-A | Noun | level 2 |  | “royal hat” |  |  |
| crucify-A | Verb | level 2 |  | “kill X [by hanging-C//putting X on-C a cross]”  If not at the moment of death, use “put X on a cross [so that X would die]”, which will NOT be converted to "crucify" | crucify X |  |
| cumin-A | Noun | level 2 |  | Level 3 word. Use a pairing or something like “spice [that causes [food to taste good]]”. |  |  |
| curse-A | Verb | level 2 |  | “X says very_optional rude//bad-B things-C/words [that are about Y]” | X curses Y |  |
| curse-B | Verb | level 2 |  | “God//Yahweh//Jesus causes [bad things to happen to Y]”. Or pair with “punish” or "harm". For X = human, or “says, [‘I pray-hope _May [bad things will happen to X]’]” “God//Yahweh//Jesus causes [many bad things to happen to Y]” | X curses Y |  |
| curse-C | Verb | level 2 |  | “X says [bad-A things will happen to Y]" | X curses Y |  |
| curse-D | Verb | level 2 |  | “X says very_optional rude words” | X curses |  |
| cushion-A | Noun | level 2 |  | "bag [that is filled by X _mayBeImplicit with soft material _inLDVAdd] of cloth" |  |  |
| cymbal-A | Noun | level 2 |  | "piece of metal [that produces a sound [when X hits piece of metal]]" |  |  |
| damage-A | Noun | level 1 |  |  |  |  |
| damage-A | Verb | level 1 | harm |  |  |  |
| daughter-in-law-A | Noun | level 2 |  | "wife of son" |  |  |
| daughter-in-law-A | Noun | level 2 |  | “wife of  X's son” | X's daughter-in-law |  |
| deacon-A | Noun | level 2 |  | “special servant of the church” |  |  |
| deacon-B | Noun | level 2 |  |  |  |  |
| deaf-A | Adjective | level 2 |  | “person [who is not able [to hear sounds]]” | deaf person |  |
| deaf-A | Adjective | level 2 |  | “X is not able [to hear sounds]” | X be-Deaf |  |
| debate-A | Verb | level 2 | Argue |  |  |  |
| declare-A | Verb | level 2 | Say |  | declare [that... ] |  |
| declare-B | Verb | level 2 | Say |  | declare [" "] |  |
| decree-A | Noun | level 2 | law//rule//command |  |  |  |
| dedicate-A | Verb | level 2 | give |  |  |  |
| deeply-A | Adverb | level 2 | much |  | sleep deeply |  |
| deer-A | Noun | level 2 | animal | In almost all cases, it would be best to pair this with "animal". If an explication is necessary, consider something like "a big wild animal [that runs fast] [that eats grass] [and that has horns]", like in the Longman Dictionary. |  |  |
| defile-A | Verb | level 2 |  | “cause [X to become religiously dirty-A]” | defile X |  |
| delight-A | Verb | level 2 | please |  |  |  |
| demolish-A | Verb | level 2 | destroy |  |  |  |
| demon-A | Noun | level 2 |  | “evil spirit,” where if you want “evil spirit,” you need to block the rule. Alternately you can use "very bad-B spirit" when you have "evil spirit" and "demon" in the same verse or possibly pair "demon" with "spirit-B" where you want "demon" , especially if the spirit has been referred to previously. like "that spirit-B/demon". |  |  |
| denarius-A | Noun | level 2 |  | “Roman silver coin” (RED: removed implicit notation for “Roman” on 12/10/21 - Implicit information can’t be used in a rule) |  |  |
| descendant-A | Noun | level 2 | Person//son//child | Suggestion: use explicit pairing with “person/descendant” or “son/descendant” or “child/descendant”, depending on the context Note: Use Son-of-David instead of “son/descendant of David” |  |  |
| desire-A | Verb | level 2 | Want | Note: “much desire -> desire greatly” | X wants Y |  |
| desire-B | Verb | level 2 | want |  | X wants [to... ] |  |
| desire-C | Verb | level 2 | want |  | X wants [Y to... ] |  |
| despise-A | Verb | level 2 | hate//laugh at |  |  |  |
| determine-A | Verb | level 2 | Learn |  | X determines Y |  |
| determine-B | Verb | level 2 |  |  | X determines [that... ] |  |
| detest-A | Verb | level 2 | hate |  |  |  |
| detestable-A | Adjective | level 2 | bad//terrible |  |  |  |
| devil-A | Noun | level 2 |  | “chief evil spirit" |  |  |
| devour-A | Verb | level 2 | Eat |  |  |  |
| dew-A | Noun | level 2 | water |  |  |  |
| dill-A | Noun | level 2 | spice | Use a pairing or something like “spice [that causes [food to taste good]]”. |  |  |
| director-A | Noun | level 2 | leader |  |  |  |
| dirty-B | Adjective | level 2 |  | “religiously dirty-A” - In English, this becomes "unclean" |  |  |
| disagree-A | Verb | level 2 |  | “not agree” |  |  |
| disaster-A | Noun | level 2 | trouble |  |  |  |
| disciple-A | Noun | level 2 |  | “man [who follows-B _routinely Jesus//Christ]” is what we currently have in the program. [] For the record, this is what I wrote previously: "Person [who follows-B _routinely Jesus//Christ]”, An alternate rule – not the default – can use "man" or "woman" instead of "person". Or pair with “follower”. |  |  |
| disciple-A | Noun | level 2 |  | "Person [who follows-B _routinely X]". [] Previously I had: An alternate rule – not the default – can use "man" or "woman" instead of "person". Or pair with “follower”. | X’s disciple (previously was not for Jesus or Christ) |  |
| disciple-A | Noun | level 2 |  | “X Follows-B _routinely Y” - NOTE: This rule should only take effect if the rule for “X’s disciple” has not taken effect. [] Previously had An alternate rule – not the default – can use "man" or "woman" instead of "person". Or pair with “follower”. | X be Y’s disciple |  |
| disciple-A | Noun | level 2 |  | “X follow (imp) Y” | X become (imp) Y’s disciple |  |
| discipline-A | Verb | level 2 | train |  |  |  |
| discipline-B | Verb | level 2 | punish |  |  |  |
| discouraged-A | Adjective | level 2 |  | "X stopped being brave//courageous" or pair  "discouraged" with "sad" | X is discouraged |  |
| distressed-A | Adjective | level 2 | upset//sad |  |  |  |
| distribute-A | Verb | level 2 | give |  |  |  |
| diviner-A | Noun | level 2 |  | "person [who says//predicts [that certain things will happen in the future]]" |  |  |
| divorce-A | Verb | level 2 |  | Generic explication: “X ends X’s marriage [that is with Y]”. Or “X sends Y from X”, where Y is husband, wife, or spouse.  Or in some cases you could pair with “leave”, | X divorces Y |  |
| donkey-A | Noun | level 2 |  | "animal [that carries people’s loads]_optional [and that is like a horse]", but in most cases, it would be better to pair "donkey" with "horse" or "animal” |  |  |
| dough-A | Noun | level 2 | bread//flour | dough = flour mixed with water (a suggestion) |  |  |
| dove-A | Noun | level 2 | bird |  |  |  |
| drachma-A | Noun | level 4 |  | “Greek silver coin” |  | (only once in Bible) |
| drag-A | Verb | level 2 | pull |  |  |  |
| dragon-A | Noun | level 2 |  | "big dangerous/fierce snake/reptile" |  |  |
| drown-A | Verb | level 2 |  | “die in water//lake//sea” |  |  |
| dwell-A | Verb | level 2 | live |  |  |  |
| eagle-A | Noun | level 2 |  | "big strong bird" |  |  |
| earnestly-A | Adverb | level 2 | much, urgently, seriously, truly, carefully |  |  |  |
| earring-A | Noun | level 2 |  | "jewelry [that a person//people _generic wears on a person//people's _generic ears]", or pair with "jewelry" | earring |  |
| earring-A | Noun | level 2 |  |  | X's earring |  |
| earthquake-A | Noun | level 3 |  | “the ground shakes violently” | be-E an earthquake |  |
| earthquake-A | Noun | level 3 |  | “the ground shakes violently at//in X _plural” | be-E earthquakes at//in X _plural |  |
| earthquake-A | Noun | level 3 |  | “the ground shakes very violently” | be-E a powerful earthquake |  |
| earthquake-A | Noun | level 3 |  | “the ground shakes very violently at//in X _plural” | be-E powerful earthquakes at//in X _plural |  |
| elder-A | Noun | level 2 |  | “old leader” but unless the fact that they are old is important, use "leader/elder" |  |  |
| emperor-A | Noun | level 2 | king |  |  |  |
| enable-A | Verb | level 2 |  | “cause [X to be able-A [to Y]]”, or pair with “help-B” | enable [X to Y] |  |
| endure-A | Verb | level 2 | stay//live//be//support//exist | "X continues to live [without complaining]". Pairing with just "live" might not be satisfactory. We have recently used "live/endure patiently" in Romans. | X endures |  |
| entrust-A | Verb | level 2 | Give |  |  |  |
| envy-A | Verb | level 2 |  | “want [to live [just-like X lives]]” or “Want [to be like X]” |  |  |
| ephod-A | Noun | level 2 |  | "cloth-B [that hangs from the chiefest priest's shoulders]" |  |  |
| erase-A | Verb | level 2 | take-away |  |  |  |
| establish-A | Verb | level 2 | cause-B//make-C//set-up |  |  |  |
| eternal-A | Adjective | level 2 |  | “X [that never ends]” or "life [that does not end]" - useful for “receive eternal life”. (Alternately you could consider using “live forever//eternally with God” where "eternally" is “forever_adverb” or “forever_adverb/eternally_adverb”.) | eternal X |  |
| eternal-A | Adjective | level 2 |  | "exists _timeless forever" | be eternal |  |
| eternally-A | Adverb | level 2 | forever |  |  |  |
| eunuch-A | Noun | level 2 |  | “man [who does not have testicles]” |  |  |
| ewe-A | Noun | level 2 |  | “female sheep” |  |  |
| exalt-A | Verb | level 2 | praise//honor | “X shows people _generic [Y is extremely great]” or “X tries [to cause [other people to think [that Y is great]]]”, or pair with “honor” |  |  |
| exile-A | Verb | level 2 |  | “the army of X take-away Y to Z” | X exiles Y to Z |  |
| explore-A | Verb | level 2 |  | "go into//through X [in order to get information [that is about X]]" or pair with "learn-C" or "examine" |  |  |
| faint-A | Verb | level 2 | fall-B | Consider adding an implicit explanation like "[because (implicit-situational) X became weak]" if just "fall-B" would not be satisfactory to represent "faint". |  |  |
| faith-A | Noun | level 3 |  | For a simple alternate or perhaps for some other reason, you consider using "believe" or "trust". [] We are now allowing "faith" to take an argument, so you can say "faith in X" | have Faith, have Faith in X |  |
| faithfulness-A | Noun | level 3 |  | A simple alternate can use “faithful”. |  |  |
| fall-prostrate-A | Verb | level 2 |  |  |  |  |
| famine-A | Noun | level 2 |  | "There are very many people [who do not have enough food]" or "There is not enough food [so that many people are dying/starving]" [] Previously “very many people [optional who live in X] do not have enough food” or “the amount of food [that was available in X] was not enough [so that many people were dying/starving]” (where “X” could include the word “land”) or “the land did not produce enough food [so that many people were dying/starving]” | be-E a famine |  |
| famine-A | Noun | level 2 |  | With X singular: "There are very many people [who do not have enough food] in X" or "There is not enough food in X [so that many people are dying/starving]" | be-E a famine at//in X _singular |  |
| famine-A | Noun | level 2 |  | With X plural: "There are very many people [who do not have enough food] in X" or "There is not enough food in X [so that many people are dying/starving]" | be-E famines at//in X _plural |  |
| farmer-A | Noun | level 2 |  | “person//man [who grows _routinely crops]” (Richard: the current rule is “man who grows crops”. This should be generalized to allow for "person".) |  |  |
| fast-A | Verb | level 2 |  | Generic: “X does not eat food" [so that X could pray]” Also, “X refuses [to eat food]” (as in wedding guests fasting from the food at a wedding). For the  negative “does not fast”,  see the entry in the next row. | X fasts |  |
| fast-A | Verb | level 2 |  | “X does not stop eating [in order to pray]" | X does not fast |  |
| father-in-law-A | Noun | level 2 |  | “father of X’s dead_optional wife//husband//spouse” | X-s father-in-law |  |
| fear-A | Noun | level 1 |  |  |  | Make simple? |
| fear-A | Verb | level 2 |  | “be afraid of X” | fear X |  |
| fear-respect-A | Verb | level 2 | respect//honor//obey//follow-B |  | fear the Lord |  |
| feast-A | Noun | level 2 |  | “big meal”. In some circumstances, you will want to pair this with "meal". In other circumstances, it will be better to pair this with “holiday”. |  |  |
| fellowship-A | Noun | level 3 |  | Suggestion: use a simple alternate with "share-B life//work" |  |  |
| fertile-A | Adjective | level 2 |  | "X that produces many crops//plants" | fertile X |  |
| fertile-A | Adjective | level 2 |  | "X produces many crops/plants" (this rule should be checked after the rule for "fertile X") | X is fertile |  |
| fierce-A | Adjective | level 2 | violent//angry//dangerous |  |  |  |
| firstborn-A | Adjective | level 2 |  | “X [who was born first]” or "first X [that was born from X's mother//father//parent]" | firstborn X |  |
| fisherman-A | Noun | level 2 |  | "person [who catch _routinely fish _generic [in order to earn money]]" |  |  |
| fisherman-A | Noun | level 2 |  | "X catches _routinely fish _generic [in order to earn money]". Note: this rule must be checked after "fishermen". | X be Fisherman |  |
| fist-A | Noun | level 2 |  | We did have the suggestion to pair this with "hand", but it's only use 8 times in the Bible. We are getting rid of it. |  |  |
| flea-A | Noun | level 2 |  |  |  |  |
| flea-A | Noun | level 2 |  | "Very small insect [that bites animals or people]" Note: the current explication is “small insect [that lives on dogs]” |  |  |
| flood-A | Noun | level 2 | water _plural | “water [that completely _optional covered-C the earth]” or pair with "water" |  |  |
| flourish-A | Verb | level 2 | succeed |  |  |  |
| flower-lily-A | Noun | level 2 | flower |  |  |  |
| flute-A | Noun | level 2 |  | "instrument that produces sound [when X blows over instrument's holes]" |  |  |
| foolish-A | Adjective | level 2 | bad-B (though “stupid” in some circumstances; the TN says it is moral foolishness in Proverbs) |  |  |  |
| foolishly-A | Adverb | level 2 | badly-B/badly/stupidly |  |  |  |
| forbid-A | Verb | level 2 |  | “tell X [X is not allowed by Z [to Y]]” where Y is a verb. | forbid [X to Y] |  |
| forehead-A | Noun | level 2 | face//head | "part of the face that is above the eyes" |  |  |
| forehead-A | Noun | level 2 |  | "part of the X's face that is above X's eyes" | X's forehead |  |
| foreign-A | Adjective | level 2 | another |  |  |  |
| foreigner-A | Noun | level 2 |  | “person [who be_birthplace//comes from an other/foreign country]”. |  |  |
| foreigner-A | Noun | level 2 |  | “be from another/foreign country” | be a Foreigner |  |
| foreskin-A | Noun | level 2 |  | Suggested: “skin [that is on the end of the penis]” |  |  |
| foreskin-A | Noun | level 2 |  | Suggested: “skin [that is on the end of X’s penis]” | X's foreskin |  |
| form-A | Noun | level 2 | shape |  |  |  |
| formless-A | Adjective | level 3 |  | include a simple alternate - "does not have shape" |  |  |
| forsake-A | Verb | level 2 | leave, ignore, avoid |  |  |  |
| fortified-A | Adjective | level 2 |  | “city//town//place [that has walls]” or pair the adjective "fortified" with "strong" | fortified city//town//place |  |
| foundation-A | Noun | level 2 |  | “bottom layer of stones” |  |  |
| fox-A | Noun | level 2 | animal |  |  |  |
| frankincense-A | Noun | level 2 |  | “very expensive incense” |  |  |
| frown-A | Verb | level 2 |  | Tentatively, “make an upset expression”, But I(Richard) am not totally happy with that |  |  |
| fruitful-A | Adjective | level 3 |  |  |  |  |
| fulfill-A | Verb | level 3 |  | pair “fulfill” (transitive) with “complete” or "keep-B" pair “be-fulfilled” (intransitive) with “happen” |  |  |
| furnace-A | Noun | level 2 |  | “big container [that contains a very hot fire]” (previously “big _optional container [that contains a very hot fire]”) |  |  |
| gall-A | Noun | level 2 |  | "a bitter substance" |  |  |
| gazelle-A | Noun | level 2 | animal |  |  |  |
| gem-A | Noun | level 2 | jewel |  |  |  |
| genealogy-A | Noun | level 2 |  | “family history” |  |  |
| generation-A | Noun | level 2 | time, or group | "group of age" = "age group"; but consider using "people of this//that time/generation" |  |  |
| Gentile-A | Noun | level 2 |  | “person [who is not a Jew]” - This rule should Require that “person” be Third person |  |  |
| Gentile-A | Noun | level 2 |  | “not be a Jew”. Note: this rule should be applied after the rule for just “Gentile” | be Gentile |  |
| germ-A | Noun | level 2 |  | "extremely small creature [that causes [a person to have a disease] [ _optionalForExplication when a small creature is in the body of a person]]" or pair with "thing-A//creature" |  |  |
| giant-A | Noun | level 2 |  | "extremely tall person//man" |  |  |
| gladly-A | Adverb | level 2 | happily |  |  |  |
| gladness-A | Noun | level 3 |  | include a simple alternate, probably using "glad" or "gladly" |  |  |
| glean-A | Verb | level 2 |  | “gather X behind workers [who are gathering/harvesting X]”, or pair it with “gather” |  |  |
| glorify-A | Verb | level 2 | praise//honor X |  |  |  |
| glorious-A | Adjective | level 2 | great |  |  |  |
| glory-A | Noun | level 3 | power//honor//reward | write simple alternate using “great/glorious” |  |  |
| gnash-A | Verb | level 2 | bite | (requested by Tod, even though “gnash” is only used 14 times in the Bible) |  |  |
| gnat-A | Noun | level 2 | insect |  |  |  |
| goblet-A | Noun | level 2 | cup |  |  |  |
| goodness-A | Noun | level 3 |  |  |  |  |
| governor-A | Noun | level 2 | ruler |  |  |  |
| grab-A | Verb | level 2 |  | “quickly take”, or pair with “hold” |  |  |
| grace-A | Noun | level 3 | gift | For a simple alternate, consider using “kind/gracious” or “kindly/graciously”. In some circumstances you can pair with "gift". For "give grace to X", consider "treat X kindly/graciously". |  |  |
| gracious-A | Adjective | level 2 | kind |  |  |  |
| graciously-A | Adverb | level 2 | kindly |  | boast(?) |  |
| grandchild-A | Noun | level 2 |  | “child of a child//son//daughter” or it might be appropriate to pair with "child//son//daughter". |  |  |
| grandchild-A | Noun | level 2 |  | "child of X’s child//son/daughter" | X’s grandchild |  |
| granddaughter-A | Noun | level 2 |  | “daughter of a child” or it might be appropriate to pair with "daughter". “X’s granddaughter = daughter of X’s child” |  |  |
| grandfather-A | Noun | level 1 |  | “father of a parent” or it might be appropriate to pair with "father". “X’s grandfather = father of X’s parent” |  |  |
| grandson-A | Noun | level 2 |  | “son of a child” or it might be appropriate to pair with "child" or "son" | grandson |  |
| grandson-A | Noun | level 2 |  | “X’s grandson = son of X’s child” or it might be appropriate to pair with "child" or "son" like "X's child/grandson" | X's grandson |  |
| grape-A | Noun | level 2 |  | “fruit [that people make wine with]”. Or perhaps in some limited cases, could pair with “fruit”. |  |  |
| greedy-A | Adjective | level 2 |  | “X always wants more Y(things//food//etc) [even-if//even-though X does not need more Y]” | X is greedy |  |
| greedy-A | Adjective | level 2 |  | “X [who always wants more Y(things//food//etc) [even-if X does not need more Y(things//food//etc)]]” | greedy X |  |
| grieve-A | Verb | level 2 |  | “be extremely sad” with the extreme feature required |  |  |
| groan-A | Verb | level 2 | cry-out |  |  |  |
| guard-A | Noun | level 2 |  | "person [who guards X _generic]”, or pair with something like ‘servant’ used for ‘guard’ in the context of the Temple or “soldier” |  |  |
| guard-A | Noun | level 2 |  | "person [who guards X _notGeneric]” | guard of X |  |
| guide-A | Noun | level 2 |  | "person [who guides people]" |  |  |
| habitually-A | Adverb | level 2 | regularly |  |  |  |
| Hades-A | Noun | level 4 |  | Previously: “place [that the spirits of dead people temporarily _implicit go to [after those people die]]" - but now level 4 (proper noun) |  |  |
| hail-A | Noun | level 2 | ice | rain [that changed into ice] |  |  |
| hang-B | Verb | level 2 |  | Generic: “kill X [by hanging X on a tree]”. Or “... hanging on a tree/pole/post” Or pair with “kill” | hang X |  |
| harbor-A | Noun | level 2 |  | “a place [that ships stay at]” |  |  |
| harp-A | Noun | level 2 |  | "instrument [that has strings-B]" or "big instrument [that has strings-B]" |  |  |
| harshly-A | Adverb | level 2 | cruelly, much |  |  |  |
| harvest-A | Verb | level 2 | gather//pick//get |  |  |  |
| heal-A | Verb | level 2 |  | “cause [X to become healthy [(optionally) so that X woulddid not have Y]]” | heal X ( _optionally from Y) |  |
| hell-A | Noun | level 2 |  | (Greek ‘Gehenna’, Hebrew ‘Gehinnom’) = “place [that evil people//people-B are punished by God _implicitActiveAgent at [after evil people _AOnly die]]” P.S. figurative extension of the Valley of Hinnom |  |  |
| hell-B | Noun | level 2 |  | (Greek ‘Hades’, Hebrew ‘Sheol’) = “place [that the spirits of dead people temporarily _implicit go to [after people die]]" |  |  |
| helmet-A | Noun | level 2 |  | “hard hat” or "hat [that protects X]" |  |  |
| history-A | Noun | level 1 |  | Try to use "story" (A sense) or  expresses some other way like with "talk about" |  |  |
| holy-A | Adjective | level 2 | special//good-B//perfect//pure(only for substances) |  |  |  |
| honey-A | Noun | level 2 |  | "sweet substance [that insects/bees make-E]" or the pairing “sugar/honey” |  |  |
| hook-A | Noun | level 2 | ring-A |  |  |  |
| hug-A | Verb | level 2 |  | “X put X’s arms around Y” = “X hugged Y” |  |  |
| humble-A | Adjective | level 2 |  | "X is not proud" or “X does not think [X is more important than other people]” or “X thinks//knows [X is not more important than other people]” | X is Humble |  |
| humble-A | Adjective | level 2 |  | "X stops being proud" or “X starts to think [X is not more important than other people]” (in this case put “not” in subordinate clause to avoid problem with scope of “not”) | X becomes Humble |  |
| hymn-A | Noun | level 2 |  | “song [that is about God]” |  |  |
| hypocrite-A | Noun | level 2 |  | Generic: “person [who pretends [to be good/righteous]]”. Also,  “person [who pretends [to be different from person]]” |  |  |
| hypocrite-A | Noun | level 2 |  | “X pretends [to be good-B/righteous]” or "X pretends [to be good-B/righteous ] [even-though X is not good-B/righteous]. Also “X pretends [to be different from X]” | X be a hypocrite |  |
| idol-A | Noun | level 2 |  | “object [that X thinks [is a god]]” or pair with “object” |  |  |
| idol-A | Noun | level 2 |  | object [that represents X] | idol of X |  |
| image-A | Noun | level 3 |  | With a simple alternate like "be/become like God" | image of God |  |
| impure-A | Adjective | level 2 | bad_morally |  |  |  |
| in-J | Adposition | level 1 |  | We suggest using this literally and then having a dynamic alternate with “have a <<good>> relationship that is with Christ”, or "united to Christ by God _implicitActiveAgent". In some cases, the dynamic alternate could express this a different way, like with “believing”. Refer to the suggestion in the TNN. | like for "in-J Christ" |  |
| incense-A | Noun | level 2 |  | “a substance [that smells good [when people burn a substance]]” |  |  |
| inherit-A | Verb | level 2 |  | “receive Y’s _optional X [when//after Y dies]” (after probably better). Or in some cases, it might be appropriate to pair “inherit” with “receive”. Tod: Change “thing” in the rule to an example (-> X). | inherit X {from Y}_optional |  |
| injure-A | Verb | level 2 | hurt | Even though it's in the LDV, we're going to keep this complex since we have a great pairing for it |  |  |
| inn-A | Noun | level 2 |  | "building [that people stay at [while people are far from people's houses]]" |  |  |
| innocent-A | Adjective | level 2 |  | “X [ _restrictive who is not guilty]” (Note: This rule should be implemented before be-Innocent) | innocent X |  |
| innocent-A | Adjective | level 2 |  | “be not be guilty” | be innocent |  |
| insist-A | Verb | level 2 | Chooses or say |  | insist [that... ] |  |
| inspire-A | Verb | level 2 | cause-B//teach |  | inspire X |  |
| instruct-A | Verb | level 2 | teach//tell |  | instruct [X to Y] |  |
| instruct-B | Verb | level 2 |  |  | instruct X |  |
| interest-A | Noun | level 2 |  | "Extra money [that a person gets [when a person loans money to another person]]" or pair with "money" |  |  |
| intestine-A | Noun | level 2 | organs |  |  |  |
| invade-A | Verb | level 2 | attack//enter |  |  |  |
| jackal-A | Noun | level 2 |  | wild dog |  |  |
| jar-A | Noun | level 2 | container or pot |  |  |  |
| jealous-A | Adjective | level 2 |  | “X wants the things(AorD) [that Y has]” for being jealous of possessions. (Also see “envy”)be | X be Jealous of Y |  |
| jealous-B | Adjective | level 2 |  | Concerning jealousy of the attention that a person gets, “X be upset [because Z likes//loves Y [more-than Z likes/loves X]]”. | X be Jealous of Y |  |
| joy-A | Noun | level 3 |  | Requires a simple alternate. But may not be necessary. Consider “happy/joyful” |  |  |
| joyful-A | Adjective | level 2 | happy |  |  |  |
| joyfully-A | Adverb | level 2 | happily |  |  |  |
| just-A | Adjective | level 2 | fair or right |  |  |  |
| justice-A | Noun | level 3 |  | include a simple alternate |  |  |
| justly-A | Adverb | level 2 | fairly |  |  |  |
| kidnap-A | Verb | level 2 |  | “X take-away Y [in order to do an evil action]". | X Kidnaps Y | Richard thinks we could get rid of it |
| kingdom-A | Noun | level 2 | country/land/area |  |  |  |
| kingdom-B | Noun | level 3 |  | Some suggestions for a simple alternate: Use the verb "rule" with something like "become people [whom God rules]", use "king" with something like "God will be their king", use "be//become people of God", or “the Kingdom of God is near” could be “the very good things [that God wants [to do]] will happen soon”. Or “lead-B” instead of “rule” may be appropriate, like for the rich man letting God lead him. |  |  |
| kingdom-C | Noun | level 2 | nation |  |  |  |
| kinsman-redeemer-A | Noun | level 4 | man | if it can’t be paired with something like “man”, it should be expressed with a simple alternate. I have been using "must(or should) protect the name of our_excl(Ruth's) family_implicit and our_excl(Ruth's) family's property_implicit" (see TN). |  |  |
| lack-A | Verb | level 3 |  | "has all the things X needs" | lack nothing |  |
| lack-A | Verb | level 3 |  | "does not have X" | lack X |  |
| lamb-A | Noun | level 2 |  | “young sheep” |  |  |
| lame-A | Adjective | level 2 |  | “person//man//woman//child//girl//boy//foot//leg [who is not able [to walk]” | lame X |  |
| lame-A | Adjective | level 2 |  | “X is not able [to walk]” | X is lame |  |
| lampstand-A | Noun | level 2 |  | "object//pole [that a lamp is on]", or in limited cases (not for the lampstand in the tabernacle), it might be paired with "table" "set of poles [that have special/holy lamps" (used for the lampstand in the tabernacle) |  |  |
| Law-A | Noun | level 2 | law-B |  |  |  |
| Law-B | Noun | level 2 | law-B |  |  |  |
| leopard-A | Noun | level 2 |  | "big wild cat [that has black circles on big wild cat's fur]" |  |  |
| leprosy-A | Noun | level 2 |  | “infectious disease [that destroys the skin and nerves]”. Warning: in the Bible, “leprosy” often is used more generally to refer to a skin disease. Consider using just “skin disease” or “terrible disease of the skin” |  |  |
| liar-A | Noun | level 2 |  | “person [who _routinelyFeature says false things” |  |  |
| liar-A | Noun | level 2 |  | “_routinelyFeature says false things” . Evaluate “liar” before this rule. | be a liar |  |
| lick-A | Verb | level 2 | taste |  |  |  |
| lie-A | Noun | level 2 |  | “False thing-C _speech” |  |  |
| lie-A | Verb | level 2 |  | Use “say false thing-C _speech” |  |  |
| ligament-A | Noun | level 2 |  | Suggestion: Use “parts/ligament of the body” |  |  |
| linen-A | Noun | level 2 |  | "good light cloth" | linen |  |
| linen-A | Noun | level 2 |  | "very good light cloth" | good linen |  |
| livestock-A | Noun | level 2 | animal | "animals of farm" (generated as "farm animals" in English) or pair with "animals" |  |  |
| locust-A | Noun | level 2 | insect | “insect [that flies] [and that eats crops] |  |  |
| long-A | Verb | level 2 | want |  | long [to ...] |  |
| lord-A | Noun | level 2 | master |  |  |  |
| lost-A | Adjective | level 2 |  | “X [that Y is not able [to find]]”, with Y = people_generic and possibly other things | lost X |  |
| lost-A | Adjective | level 2 |  | "Y be not able [to find X]" - Note: rule must check for "lost X" first | X be lost |  |
| lot-A | Noun | level 2 |  | “stone [that has-F marks]”, or pair with “stick//stone//bone” |  |  |
| lust-A | Verb | level 2 | want |  |  |  |
| lyre-A | Noun | level 2 |  | "small instrument [that has strings]", or pair with "instrument" |  |  |
| magician-A | Noun | level 2 |  | “person//man [who uses magic]” (not used with “woman -> witch”) Same as “sorcerer” |  |  |
| manger-A | Noun | level 2 |  | “box [that contained food for big farm animals]” |  |  |
| manuscript-A | Noun | level 2 | copy |  |  |  |
| marble-A | Noun | level 2 |  | hard smooth stone |  |  |
| march-A | Verb | level 2 | walk//go//come |  |  |  |
| mason-A | Noun | level 2 |  | Suggestion: “person [who builds things with stones]” |  |  |
| mat-A | Noun | level 2 | bed |  |  |  |
| mature-A | Adjective | level 2 | strong//healthy | Or consider saying it differently without using "mature" |  |  |
| meditate-A | Noun | level 2 | think-A//consider-A |  |  |  |
| merchant-A | Noun | level 2 |  | “person [who sells things]” |  |  |
| merciful-A | Adjective | level 2 | Kind |  |  |  |
| merciful-B | Adjective | level 2 |  |  |  |  |
| mercy-A | Noun | level 3 |  | usually use simple alternate with “kind/merciful” |  |  |
| messenger-A | Noun | level 2 |  | “Person//servant [who takes messages to people _generic]”. Richard: The current rule is “carries messages”, but “takes” is more general. |  |  |
| messenger-A | Noun | level 2 |  | “Person//servant [who takes X’s messages to people _generic]”. Richard: The current rule is “carries messages”, but “takes” is more general. | messenger of X |  |
| midnight-A | Noun | level 4 |  | “the middle-C of the night” or we could add “12AM” |  |  |
| mint-A | Noun | level 2 |  | “green leaves [that cause [food to taste good]]” or pair with “spice” or “leaves” |  |  |
| miracle-A | Noun | level 2 |  | Default explication: "an event//action [that only God is able [to do]]". We also have a rule that "action [that X does through God's power] -> miracle [that X did]". Also “by using God’s poweraction [that X does [] -> miracle [that X did]”. Note: You can use the passive to hide the agent "X" as long as you specify with "by X". |  |  |
| miracle-A | Noun | level 2 |  | “X does an (optionally with an adjective here) action through God's power". Also there is currently a rule "X does an action [by using God's power]". Note: You can use the passive to hide the agent "X" as long as you specify with "by X". | X do miracle |  |
| miserable-A | Adjective | level 2 | sad//upset |  |  | (though it's only used four times) |
| mock-A | Verb | level 2 | Laugh_B (laugh at) |  |  |  |
| mold-A | Noun | level 2 | disease |  |  |  |
| moth-A | Noun | level 2 | insect | Or “insect/moth [(Implicit-background) that flies” or with some other implicit information if necessary |  |  |
| mother-in-law-A | Noun | level 2 |  | "mother of dead _optional spouse//wife//husband" |  |  |
| mother-in-law-A | Noun | level 2 |  | “mother of X's dead_optional spouse//wife//husband” | X's mother-in-law |  |
| motive-A | Noun | level 2 |  | Suggestion: try to use “reason//purpose” |  |  |
| mourn-A | Verb | level 2 | cry |  |  |  |
| mourn-B | Verb | level 2 |  | “be mournful” (For phase 1, use “be sad/mournful”J) |  |  |
| mournful-A | Adjective | level 2 | sad |  |  |  |
| mule-A | Noun | level 2 |  | “animal [that has parents [that are a horse and a donkey//an animal [that is like a horse]”, but in most cases would be better to pair with “animal” or “horse” |  |  |
| multiply-A | Verb | level 2 | increase |  |  |  |
| murder-A | Verb | level 2 | kill |  |  |  |
| mute-A | Adjective | level 2 |  | “X is not able [to speak]” | X is mute |  |
| myrrh-A | Noun | level 2 |  | “expensive substance [that smells good]”  Alternate rule when used as a medicine: “expensive substance [that people use [so that people would not have much pain]]” or for burial, “expensive substance [that people put on bodies]” |  |  |
| mystery-A | Noun | level 2 |  | "thing-D [that people do not understand]" or "thing-D [that people did not previously understand]". |  |  |
| naked-A | Adjective | level 2 |  | “X [that is not wearing clothes]” | naked X |  |
| naked-A | Adjective | level 2 |  | “X is not wearing clothes” | X is naked |  |
| necklace-A | Noun | level 2 | chain |  |  |  |
| neighbor-A | Noun | level 2 | friend | “person [who lives near X]”. Note: “neighbor” in the Bible might have a more general meaning. | X's neighbor |  |
| Nephilim-A | Noun | level 2 |  | Suggestion: use "giant" (see the entry) |  |  |
| noble-A | Adjective | level 2 | good |  |  |  |
| noble-A | Noun | level 2 |  | "person//man of honor" or pair with "man//person//ruler" |  |  |
| nurse-A | Verb | level 2 |  | "X gives milk from X's breast to Y". Currently: “X gives X’s milk to her child//baby” | X nurses Y |  |
| oath-A | Noun | level 2 | promise |  |  |  |
| obtain-A | Verb | level 2 | get |  |  |  |
| offering-A | Noun | level 2 | gift |  |  |  |
| oil-olive-A | Noun | level 2 | oil |  |  |  |
| olive-A | Noun | level 2 | fruit | "fruit [that a tree-olive produces]" |  |  |
| onyx-A | Noun | level 2 |  | “stone-B _1 [that has different colors]” |  |  |
| oppress-A | Verb | level 2 |  | “treat _routine cruelly”, “much oppress = treat _routine very cruelly” |  |  |
| orphan-A | Noun | level 2 |  | "child//person [who does not have parents [because child's parents  died]]". Old: “child [who has parents  [who died]]”. Note: For singular "orphan", make "parents" dual. |  | (though only 4 times in Bible) |
| oven-A | Noun | level 2 |  | place [that food is baked in] |  |  |
| overflow-A | Verb | level 3 |  |  |  |  |
| oversee-A | Verb | level 2 | manage |  |  |  |
| overseer-A | Noun | level 2 |  | "chief leader" |  |  |
| overseer-B | Noun | level 2 | manager//master//leader |  |  |  |
| overwhelmed-A | Adjective | level 2 | upset//sad |  |  |  |
| owner-A | Noun | level 2 |  | “person [who owns X]” | X's owner |  |
| ox-A | Noun | level 2 | Cow | “cow [that people use [in order to do work]]” - but in most cases, try to pair with "cow". |  |  |
| palace-A | Noun | level 2 |  | “royal house” or pair with “house” for high priest’s house |  |  |
| pan-A | Noun | level 2 |  | “container [that has a handle]” |  |  |
| parable-A | Noun | level 2 | lesson | “story-B//story-A? [that teaches a lesson]”. Or pair with "story" or "lesson". |  |  |
| paralyzed-A | Adjective | level 2 |  | “be not able [to move X’s legs//bodies]”. Note: This rule should be checked after the rule for "paralyzed X". | X is paralyzed |  |
| paralyzed-A | Adjective | level 2 |  | “X [that is not able [to move X’s legs//bodies]]” | paralyzed X |  |
| pasture-A | Noun | level 2 |  | “'field [that animals eat grass in]” |  |  |
| pearl-A | Noun | level 2 | jewel |  |  |  |
| penny-A | Noun | level 2 | coin | “coin [that is least valuable]”, or use the pairing |  |  |
| perfume-A | Noun | level 2 |  | “oil [that smells good]” |  |  |
| perish-A | Verb | level 2 | die//end |  | may mean die or be destroyed or ruined |  |
| persecute-A | Verb | level 2 |  | “treat X cruelly regularly” |  |  |
| perverse-A | Adjective | level 2 | evil//wrong//bad-B |  |  |  |
| Pharaoh-A | Noun | level 2 | king |  |  |  |
| pierce-A | Verb | level 2 | enter | “make a hole through//in X with Y (optional)” | pierce X with Y (optional) |  |
| pigeon-A | Noun | level 2 | bird |  |  |  |
| pillar-A | Noun | level 2 | post |  |  |  |
| pit-A | Noun | level 2 | hole |  |  |  |
| pitcher-A | Noun | level 2 | container |  |  |  |
| plague-A | Noun | level 2 |  | "event//disaster [that causes [many people to suffer]]" or pair with "event"; (if specifically a disease kind of plague, use "disease [that kills many people]" - if this occurs frequently, we can consider adding a new sense of "plague") |  |  |
| platter-A | Noun | level 2 |  | Suggestion: “big plate” |  |  |
| plead-A | Verb | level 2 | ask//argue | Suggestion: 'plead = urgently asking' |  |  |
| plot-A | Verb | level 2 | plan | Or 'X planned [to do bad things to Y]' changes to 'X plotted against Y' if the complex concept 'plot' has been activated (from Tod’s comment). | X plots against Y |  |
| plot-B | Verb | level 2 | plan |  | X plots [to Y] |  |
| plow-A | Verb | level 2 |  | “X cuts Y [so that X could plant seeds in Y]” or ““X cuts Y [in order to plant seeds in Y]” |  |  |
| plow-A | Noun | level 2 |  | "big tool [that X cuts Y with [(so that X could)//(in order to) plant seeds in Y]]" or just  "big tool [that X cuts ground//field with]" |  |  |
| pomegranate-A | Noun | level 2 |  | “round fruit [that has many small red seeds]” or pair with “fruit” |  |  |
| pond-A | Noun | level 2 |  | “small lake” or pair with “lake” |  |  |
| portion-A | Noun | level 2 | part |  |  |  |
| preach-A | Verb | level 2 | tell-D, teach-B, |  | preach X |  |
| preach-B | Verb | level 2 | tell-C, teach-A |  | preach about X |  |
| preach-C | Verb | level 2 |  |  | preach [that X... ] |  |
| precious-A | Adjective | level 2 | valuable |  |  |  |
| predict-A | Verb | level 2 | know//say//tell |  |  |  |
| pregnant-A | Adjective | level 2 |  | “X have//get a baby in X’s body/womb” | X be//become Pregnant |  |
| priest-A | Noun | level 1 |  | "chiefest priest" (not complex) | high priest |  |
| prince-A | Noun | level 2 |  | “king’s son” |  |  |
| prince-A | Noun | level 2 |  | “son of the king of X”. Note: There has to be a rule that will convert the structure here so that “of X” is shifted to “prince” | Prince of X |  |
| proclaim-A | Verb | level 2 | say//tell |  | X proclaims [that... ] |  |
| proclaim-B | Verb | level 2 | say |  | X proclaims [" "] |  |
| proclaim-C | Verb | level 2 | talk about//tell about//speak about |  | X proclaims Y |  |
| prophecy-A | Noun | level 2 | message | Or use the verb form, "prophesy" |  |  |
| prophesy-A | Verb | level 2 |  | “say God’s//the Lord’s-A message to people _generic” NOTE: this rule must occur after “prophet” and “be-prophet” | prophesy |  |
| prophesy-A | Verb | level 2 |  | “say God’s//the Lord’s-A message to X” NOTE: this rule must occur last after “prophet” and “be-prophet” and the structure for "prophesy"  using generic people | prophesy to X |  |
| prophet-A | Noun | level 2 |  | "person//man//woman//servant [who tells God's//the Lord’s-A messages to people _genericOptional]".  [] For specialized purposes use an explicit description (not converted to “prophet”) like "person//man//woman [who tells a god's messages to people]" or "person//man [who says/claims [that that person//man tells a god's messages to people]]", depending on the context | prophet |  |
| prophet-A | Noun | level 2 |  | "person//man//servant [who tells X's messages to people _generic]" | prophet of X |  |
| prophet-A | Noun | level 2 |  | “tell _routinelyRequired God's messages to people _generic" (required because of “prophesy”) | be-Prophet | I do not think that _routinely shoud be required because there are some who were called prophets who only prophesied one time. We can solve this problem by using a different speech word for "prophesy". I suggest using "say". This will allow us to use _routinely if it is correct, or leave it off if it is not applicable. |
| prophet-A | Noun | level 2 |  | "person [who tells false messages [that are-T not from God] to people]" (Note: previously we had "... messages [that do not come from God", but we shouldn't use "come" in this way.) | False prophet | will become "false prophet" |
| prophet-A | Noun | level 2 |  | “tell _routinelyRequired false messages _generic [that do not come from God] to people _generic” | be a false prophet | will become "be false prophet" |
| prosper-A | Verb | level 2 | succeed |  |  |  |
| prosperous-A | Adjective | level 2 | successful |  |  |  |
| prostitute-A | Noun | level 2 |  | Usually “woman//person [who sexes men//people for money]”. But for male prostitutes, “man [who sexes people//women//men for money]” |  |  |
| proverb-A | Noun | level 2 | if plural, words; if singular, message |  |  |  |
| province-A | Noun | level 2 |  | Pair with something like area or country or define more specifically |  |  |
| pure-B | Adjective | level 2 | good-B |  |  |  |
| purse-A | Noun | level 2 |  | "bag [that X keeps money in]" |  |  |
| pursue-A | Verb | level 2 | chase//follow |  |  |  |
| quail-A | Noun | level 2 |  | "small fat bird" or pair with "bird" |  |  |
| quarrel-A | Verb | level 2 | argue | “argue angrily” or pair with “argue” |  |  |
| rage-A | Noun | level 2 | anger |  |  |  |
| rainbow-A | Noun | level 2 |  | "a big curve [that appears in the sky] of different colors" |  |  |
| raisin-A | Noun | level 2 |  | "dry grape" - see "grape" for how to represent it |  |  |
| ram-A | Noun | level 2 |  | “male sheep”. Or can pair with “sheep” |  |  |
| rape-A | Verb | level 2 |  | “X forces [Y to sex X]” |  |  |
| raven-A | Noun | level 2 | bird | “big_optional black bird” |  |  |
| rebel-A | Verb | level 2 | Fight-A//oppose | Note to P2: In "rebel X" generated as "rebel against X", X should be a patient argument to agree with the structure for "fight" |  |  |
| rebel-A | Noun | level 2 |  |  |  |  |
| rebellious-A | Adjective | level 3 |  | Use a simple alternate with something like "does not do" or "refuses to do" or "opposes". |  |  |
| rebuke-A | Verb | level 2 |  | “tell X [the thing//things [that X did//said] are//were bad-B//bad-A//wrong]” or “tell X [X’s actions are//were bad-B//bad-A//wrong]”. Previously we said that you could pair this with "oppose", but the argument structure is different. So use the explication. |  |  |
| recline-A | Verb | level 2 | lie |  |  |  |
| reconcile-A | Verb | level 2 |  | "cause [X to again have a good relationship with Y]" | Reconcile X to Y |  |
| redeem-A | Verb | level 2 | buy//save//protect//defend | Pair with “buy”or “save” or “protect” or “defend” or write your own explication if necessary |  |  |
| redeem-B | Verb | level 2 | buy |  |  |  |
| reed-A | Noun | level 2 | branch//stick//grass |  |  |  |
| refuge-A | Noun | level 2 |  | "place [that people _genericAndPluralRequired are able-B [to be safe in]]" or pair with shelter//place//city//etc | refuge |  |
| refuge-A | Noun | level 2 |  | "place [that X is able-B [to be safe in]]" with X something other than “people” | X's refuge |  |
| region-A | Noun | level 2 | area or place |  |  |  |
| regret-A | Verb | level 2 |  | “X is sorry [that something happened] | X regrets that something happened |  |
| reign-A | Verb | level 2 | live |  |  |  |
| reject-A | Verb | level 2 |  | “Refuse [to accept X]” Could also pair with things like “ignore” or “hate”, as in “You ignore/reject God’s message” in Mark 7:13 (based off TNN alternatives). |  |  |
| rejoice-A | Verb | level 2 |  | “Be very joyful”. Rules will convert “be very joyful” to “rejoice” and “be extremely joyful -> much rejoices”. (Or a collocation rule could change this to “rejoice greatly”.) “Joyful” is paired with “happy”, so write “be very happy/joyful” in the phase 1. “Become very joyful” should become “start rejoicing”. |  |  |
| repent-A | Verb | level 2 |  | Preferred: "X changes the thoughts and the actions of X _coordinate [so that the thoughts and the actions of X _coordinate would please God//Yahweh//Lord]”. Or, "X changes X’s thoughts and X’s actions [so that X’s thoughts and X’s actions would please God//Yahweh//Lord]” | X repents |  |
| repent-A | Verb | level 2 |  | "X changes-E X's thoughts _optional and X's actions to thoughts _optional and actions [that _coordinate please God//Yahweh//Lord] from Y _optional" [] See the note at the end of the explication for "X repents" | X repents from Y |  |
| reptile-A | Noun | level 2 | snake// animal | Suggestion: in some cases you might try to include some description of the particular animals |  |  |
| require-A | Verb | level 2 | demand//make |  | require [someone to do something] |  |
| rescue-A | Verb | level 2 | save |  |  |  |
| restore-A | Verb | level 2 |  | “cause X to become like a new X” or pair with “build” or “repair” | restore an object |  |
| resurrection-A | Noun | level 3 |  | You can use an explication,“the time [that dead people _generic will become alive again at]”, or use complex/simple alternates | The resurrection (of all people/believers) |  |
| resurrection-A | Noun | level 3 |  | Use complex/simple alternates, with something like “Jesus becomes alive again” or “God causes [Jesus to become alive again]” or something similar in the simple alternate. Previous solution: “the time [that Jesus became alive again at]” (doesn’t work well in some places, if in any) | Jesus' resurrection |  |
| reveal-A | Verb | level 2 | show | Use pairing. (As suggested by Tod. Not in LDV, but used 80 times in the Bible.) |  |  |
| revenge-A | Verb | level 2 | punish//oppose |  | take-Revenge-on (I would say to use “avenge”, but in English, you usually say “avenge oneself” with different argument structure |  |
| reward-A | Verb | level 2 |  | “give a reward to X” | reward X |  |
| reward-A | Verb | level 2 |  | “give a big//great//wonderful reward to X” | much reward X |  |
| riddle-A | Noun | level 2 | story//message |  |  |  |
| righteous-A | Adjective | level 2 | good-B |  |  |  |
| righteously-A | Adverb | level 2 | well-B |  |  |  |
| righteousness-A | Noun | level 3 |  | In many cases, I would recommend using the adjective form, with “good/righteous”. If you really need to use the noun form, there should be a simple version using the adjective form. |  |  |
| riot-A | Verb | level 2 |  | “group of X(people//men) are//become violent” with “group of” removed. Note to P2: when implementing this rule, copy the time,aspect, mood, and polarity of “be//become” to “riot”. | X riots |  |
| riot-A | Verb | level 2 |  | “group of X(people//men) are//become violent [because group of people//men oppose Y]" with “group of” removed. Previously: “X meet violently [ _optional in order to oppose Y]”. Note to P2: when implementing this rule, copy the time,aspect, mood, and polarity of “be//become” to “riot”. | X riots against Y |  |
| ripe-A | Adjective | level 2 |  | “X be ready [so that people could eat that X]” | X is ripe |  |
| ripe-A | Adjective | level 2 | ready | But see “be-Ripe” |  |  |
| roast-A | Verb | level 2 | Cook |  |  |  |
| robe-A | Noun | level 2 | clothes or coat |  |  |  |
| rod-A | Noun | level 2 | stick-B | Use pairing |  |  |
| rooster-A | Noun | level 2 |  | “male chicken” |  |  |
| row-A | Verb | level 2 | move |  |  |  |
| rumor-A | Noun | level 2 | report |  |  |  |
| rush-A | Verb | level 2 | run |  |  |  |
| rust-A | Noun | level 2 |  | “brown substance [that forms on wet metal]” |  |  |
| Sabbath-A | Noun | level 2 |  | "day of rest".  For "Sabbath year", use "year of rest/Sabbath =  Sabbath year". [] Old explication: “seventh day of the week” |  |  |
| sackcloth-A | Noun | level 2 |  | “clothes of _madeOf rough cloth”. Currently there is an alternate rule, “clothes [that X wears [in order to show Y _mayBeImplicit [that X is sad]]]". |  |  |
| sacred-A | Adjective | level 2 | special//religious | Like “holy”, but used for pagan things . You can use "holy" for non-pagan things. |  |  |
| sacrifice-A | Noun | level 2 | animal, gift or meat | Suggestion: pair with “gift” or “animal” or use an explication like “animal [that a person gives to God//Yahweh [so that the priest would//could kill that animal]]” |  |  |
| sacrifice-A | Verb | level 2 |  | "kill X [in order to give X to God//Yahweh]" or “give an animal to God//Yahweh [so that a priest would kill that animal]” Or pair with “give” or “kill”. |  |  |
| sacrifice-A | Verb | level 2 |  | "kill X [in order to give X to Y]" with Y something other than God//Yahweh. Or pair with “give” or “kill”. | sacrifice X to Y |  |
| saddle-A | Noun | level 2 |  | "seat [that is on a horse//animal]" or pair with "seat" |  |  |
| sail-A | Verb | level 2 | go//move//travel |  |  |  |
| sailor-A | Noun | level 2 |  | "man [who works on a ship]" |  |  |
| saint-A | Noun | level 2 |  | “special/holy person” |  |  |
| salvation-A | Noun | level 3 |  | Supply a simple alternate with “save” |  |  |
| sandal-A | Noun | level 2 | Shoe |  |  |  |
| save-C | Verb | level 2 |  | “save-A X from bad-B action-B and death” or “save-A X from bad-B actions and death” or “save-A X from the results of X’s bad-B actions” |  |  |
| savior-A | Noun | level 3 |  | "person (AB or C) [who saves-C many people _generic]", using one of the explications for “save-C”, OR use a complex alternate (if necessary) | Savior |  |
| savior-A | Noun | level 3 |  | "person (AB or C) [who saves-C X]”, using one of the explications for “save-C”, OR use a complex alternate (if necessary) | X's Savior |  |
| saw-A | Noun | level 2 |  | "tool [that is used by people _implicitActiveAgent _genericNecessary [in order to cut wood]]" or "tool [that has sharp teeth-B]" |  |  |
| saying-A | Noun | level 2 | words//thing-C//command//message |  |  |  |
| scale-A | Noun | level 2 |  | “device [that weighs things-A]” |  |  |
| scarlet-A | Adjective | level 2 |  | "bright red" |  |  |
| scepter-A | Noun | level 2 | stick-B |  |  |  |
| scorn-A | Verb | level 2 | insult/ignore/hate/laughed at | See also the entry for “revile” |  |  |
| scorpion-A | Noun | level 2 |  | "Poisonous creature [that stings X]" (The previous explication used the noun sting, "dangerous creature [that has a poisonous sting]". With the new explication, we don't need to add that word.) |  |  |
| scout-A | Verb | level 2 | look at//examine |  |  |  |
| scream-A | Verb | level 2 |  | “X shouts [because X is very afraid]”. Or pair with something like “cry-out”. |  |  |
| scribe-A | Noun | level 2 |  | “Person//man [who teaches the law-B/Law-A {OPTIONAL: to people _generic}” . Or we also have an explication “person//man [who knows the law-B]” that could be used explicitly. Note: Previously used “religious laws”. |  |  |
| scripture-A | Noun | level 2 |  | “God’s book” -> “the Scripture” singular. A theta grid rule can change this to the plural. |  |  |
| scroll-A | Noun | level 2 |  | I suggest usually pairing with “book”. If an explication is needed, “paper//parchment [that people rolled] [and that people wrote words//books//things _implicitGeneric on]” |  |  |
| seal-A | Noun | level 2 | mark/sign |  |  |  |
| secure-A | Adjective | level 2 | safe//strong//solid |  |  |  |
| securely-A | Adverb | level 2 | tightly//well |  |  |  |
| seduce-A | Verb | level 2 |  | “X causes [Y to sex X]” | X seduces Y |  |
| seek-A | Verb | level 2 | Search for X |  |  |  |
| seize-A | Verb | level 2 | hold//take//take-away |  |  |  |
| selfish-A | Adjective | level 2 |  | “X cares about only X” | X is selfish |  |
| selfish-A | Adjective | level 2 |  | “a/that person [who cares about only a/that person]” | selfish X |  |
| shave-A | Verb | level 2 | cut-off | "X cut-off the hair from X's face" | X shaved |  |
| shave-B | Verb | level 2 | cut-off |  |  |  |
| shawl-A | Noun | level 2 | coat |  |  |  |
| sheaf-A | Noun | level 2 |  | “group of plants [that were cut by people_implicit]” for automatic, or more generally “group of plants/stalks/barley [that X cut/harvest]” |  |  |
| Sheol-A | Noun | level 4 |  | We are changing this to a proper noun. Previously the explication was “the place [that the spirits of dead people temporarily _implicit go to [after people die]]" |  |  |
| shepherd-A | Noun | level 2 |  | “person [who _routinely cares for sheep]” or “be Shepherd -> Cares for sheep” |  |  |
| shepherd-A | Verb | level 2 |  | X cares for Y [just like a person [who _routinely cares for sheep] cares for sheep]”; or in some cases you might pair it with “care for” | X shepherds Y |  |
| shield-A | Noun | level 2 |  | “a big//flat piece of metal//wood//leather [that a person//soldier holds in front of a person//soldier]” Or pair with "board-A" |  |  |
| shield-A | Noun | level 2 |  | "X's board-A [that X holds in front of X [in order to protect X]]" | X's shield |  |
| shriveled-A | Adjective | level 2 | dry |  |  | (because it’s already there, but it’s used very infrequently) |
| sickle-A | Noun | level 2 | tool or  blade |  |  |  |
| sigh-A | Verb | level 2 |  | “X breathes slowly and loudly/deeply [ _optional because X is upset//troubled//tired//sad]". The optional “because” clause is highly recommended, but if you don't know what the emotion is, you can leave it off |  |  |
| silent-A | Adjective | level 2 | quiet |  |  |  |
| sin-A | Noun | level 2 |  | “bad-B action” (representing a specific sin). |  |  |
| sin-A | Verb | level 2 |  | “Do bad-B thing-B//action”. This is for specific sins, not sin-B. If you want to indicate participant tracking (a//that//those sins), use “do bad-B thing-B//action” and block sin_verb (This will become “commit a sin” in English). An older explication is “live badly-B”. |  |  |
| sin-A | Verb | level 2 |  | "do bad-B things-B//actions [that offend  X]" or “do bad-B things-B//actions TO X -> sin AGAINST X” | sin against X |  |
| sin-B | Noun | level 2 |  | "bad-B action-B" (representing collective sin) |  |  |
| sinful-A | Adjective | level 2 | evil//bad-B//wrong |  |  |  |
| sinner-A | Noun | level 2 |  | Use “person/man/woman [who does _routine bad-B _morally things(that is, sins_verb)]”. The current rule is “Noun who does things [that God hates]” or “Noun who lives badly” (should be “badly-B”) |  |  |
| sinner-A | Noun | level 2 |  | "X does _routinely bad-B _morally things(that is, sins_verb)]” - check rule for just "sinner" first | X be a sinner |  |
| sister-D | Noun | level 2 |  | See the explication for "brother-D" which covers the most common usage. In other circumstances, you might pair this word with "woman". | (believer) |  |
| skull-A | Noun | level 2 |  | “the bones of a person's head” |  |  |
| skull-A | Noun | level 2 |  | “the bones of X’s head” | X's skull |  |
| slander-A | Verb | level 2 |  | “say evil(optional) and false things-C about X” or “say evil(optional) and false things-C [that are about X]” |  |  |
| slaughter-A | Verb | level 2 | kill |  |  |  |
| sleepy-A | Adjective | level 2 | tired |  |  |  |
| sling-A | Noun | level 2 | rope |  |  |  |
| sling-A | Verb | level 2 | throw-A |  |  |  |
| snare-A | Noun | level 2 | trap |  |  |  |
| son-B | Noun | level 2 | child//son-A |  | Son-B (literal son or dynamic child) |  |
| sorcerer-A | Noun | level 2 |  | Suggestion: “person//man [who uses magic]”, or using “magic of evil spirits” (not used with “woman -> witch”) Same as “magician” |  |  |
| sore-A | Noun | level 1 |  |  |  |  |
| soul-A | Noun | level 3 | heart//mind//spirit | I think that most often "X's soul" could just become "X". Or if it were important to say that it's the non-physical part of a person, perhaps "part of X [that is not physical]". |  |  |
| sparrow-A | Noun | level 2 | bird |  |  |  |
| spear-A | Noun | level 2 |  | “pole [that has a sharp point/tip] [and that (implicit-situational) is a weapon]_optional” |  |  |
| spiritual-A | Adjective | level 2 | religious//null |  |  |  |
| sponge-A | Noun | level 2 | cloth | I think we could eliminate this word and just use "cloth". It only occurs three times in the Bible for the same incident. |  |  |
| spouse-A | Noun | level 2 |  | "husband or wife" |  |  |
| spouse-A | Noun | level 2 |  |  | X's spouse |  |
| spring-A | Noun | level 2 |  | "place [that water come-out from the ground at]" |  |  |
| sprinkle-A | Verb | level 2 | put//throw-E |  |  |  |
| sprout-A | Verb | level 2 | grow-E/sprout |  |  |  |
| spy-A | Noun | level 2 |  | "person//man//woman  [who secretly gets information [that is about other people _genericRequired]]" |  |  |
| square-A | Noun | level 2 | market//center |  |  |  |
| stab-A | Verb | level 2 | kill, cut |  |  |  |
| stable-A | Noun | level 2 |  | “building [that baby_optional animals//cows live in]” |  |  |
| staff-A | Noun | level 2 | stick/staff | “stick [that a person uses [in order to help that person [to walk]]]” or pair with “stick” |  |  |
| stare-A | Verb | level 2 | look (at) | And see entry for “intently” |  |  |
| starve-A | Verb | level 2 | die | die [because X does not have food] |  |  |
| statue-A | Noun | level 2 |  | model//object that has the shape/form of X |  |  |
| stir-A | Verb | level 2 | turn //move |  |  |  |
| stone-A | Verb | level 2 |  | “throw stones at X in order to kill X” (new default); older rule “kill X [by throwing stones at X]”' also, for situations for which the stoning was unsuccessful, "try [to kill X] [by throwing stones at X]" | stone X |  |
| storeroom-A | Noun | level 2 |  | “room//building [that X stores things in]” |  |  |
| strap-A | Noun | level 2 | string//rope |  |  |  |
| straw-A | Noun | level 2 |  | “long dry grass” or pair with “grass” |  |  |
| stubborn-A | Adjective | level 3 |  | "X is not willing [to change]]" Or use it in a complex alternate | X is stubborn |  |
| stumble-A | Verb | level 2 |  | "begin//start to fall-B" or pair with fall-B (if you want "begin//start to fall", block this rule) |  |  |
| submit-A | Verb | level 3 | obey//respect//fear-respect | (In Ephesians, Richard used "be willing to obey" as a simple alternate to "submit" for wives and slaves. But for God, I would use the pairing with "obey".) |  |  |
| successful-A | Adjective | level 1 |  | Try to use "succeed" |  |  |
| sulfur-A | Noun | level 2 |  | "a yellow substance [that burns]" |  |  |
| sulfur-A | Noun | level 2 |  | "burn-C a yellow substance" | burn-C sulfur |  |
| sunrise-A | Noun | level 2 |  | “sun [that is rising]” also “time [that the sun rises at]” - choose which explication depending on the context, first for “sunrise is beautiful” and second for “they woke at the sunrise” |  |  |
| sunset-A | Noun | level 2 |  | Suggestion: "time [that the sun sets at]" |  |  |
| swear-A | Verb | level 2 | promise |  | swear [that... ] |  |
| swear-B | Verb | level 2 |  |  | swear [" "] |  |
| synagogue-A | Noun | level 2 |  | "small building [that Jews//people honor//worship God//Yahweh//Lord-A in]" (to use "worship", pair it with "honor") Alternate rule "small_optional religious _optional building [that Jews meet in]"  Note: This is a change from what we were previously using "small Jewish church" because we made "church(building)" level 2. |  |  |
| tabernacle-A | Noun | level 2 |  | “special/holy tent”, or pair with “tent” (when it is clear from the context what kind of “tent” this is, e.g. when the explication has already been used) |  |  |
| tablet-A | Noun | level 2 |  | “flat stone-A [that a person//Yahweh writes things-C _optionallyImplicit on]”. Note that previously we had "a flat piece of stone [that a person writes things-C _optionallyImplicit on]" |  |  |
| tax-collector-A | Noun | level 2 |  | “person//man [who collects taxes]” |  |  |
| tax-collector-A | Noun | level 2 |  | “X (routinely) collects taxes” | X be tax collector |  |
| teacher-A | Noun | level 2 | master | “person//man [who teaches-A//B things _generic to people _generic]” | teacher |  |
| teacher-A | Noun | level 2 |  | “person//man [who teaches-A//B things _generic//anything implicit to X]”. | X’s Teacher |  |
| teacher-A | Noun | level 2 |  | “person//man [who teaches-A//B people _generic about X]” | Teacher of X(a subject) |  |
| teaching-A | Noun | level 2 | message//words//thing-C |  |  |  |
| teaching-A | Noun | level 2 |  | “things-C [that X teaches]” | X’s Teaching |  |
| temple-A | Noun | level 2 |  | "big building {of Jerusalem}_optional [that Jews//Israelites//people//Jesus honor//praise//serve/worship God//Yahweh//Lord-A in]" or pair with "house" or "building" |  |  |
| temple-C | Noun | level 2 |  | "building [that people honor/worship other//their _optional gods in]" |  |  |
| temple-C | Noun | level 2 |  | "building [that people honor/worship X in]" | X's temple |  |
| tempt-A | Verb | level 2 |  | Generic: “tell X [to do bad-B things _generic]”. In other cases, you might want to use a different explication like “try [to cause [X to do bad-B things _ generic]]” or could be paired with "test". | tempt X |  |
| terrify-A | Verb | level 2 |  | "extremely much frighten" |  |  |
| testify-A | Verb | level 2 | show//tell |  | X testifes to Y [that... ] |  |
| testify-B | Verb | level 2 | speak |  | X testifies to Y about Z |  |
| testimony-A | Noun | level 2 | message//thing-C |  |  |  |
| thorn-A | Noun | level 2 |  | "Sharp points [that are on X(branch//bush//plant//vine)] -> thorns [that are on X]" |  |  |
| thorny-A | Adjective | level 2 |  | "X(branch//bush//plant//vine) [that has sharp points] -> thorny X". Note: see "brier" also | thorny X |  |
| threaten-A | Verb | level 2 | scare/threaten -suggestion (a storm threatens) | "X says to Y [X will punish//hurt//harm Y [if Y ...] _optional]" |  |  |
| thresh-A | Verb | level 2 |  | “separate X from the plants” for automatic substitution, or “separate X from plants/stalks” | thresh X |  |
| threshing-floor-A | Noun | level 2 |  | Generic: “place [that people separate _routinely grain from plants at]”. if you want more specific language, explicitly use “place [that people separate grain/barley from plants/stalks at]”. |  |  |
| throne-A | Noun | level 2 |  | “king’s chair” or "royal chair" |  |  |
| thunder-A | Noun | level 1 |  | a loud sound [that happens during a storm [that has lightning]] |  |  |
| tip-A | Noun | level 2 | end//point |  | Note: "point" would be just as good |  |
| tithe-A | Noun | level 2 | tenth |  |  |  |
| tithe-A | Adjective | level 2 |  | ***Don't use this. Use "tenth/tithe" |  | concept to be removed |
| tomb-A | Noun | level 2 |  | Use “hole//cave//[stone _optional] structure [that X puts bodies-A//corpse (with corpse from writing bodies-A/corpse) into]” or with “[and that was in stone//the ground]”. The head noun and the word “body” should match in number. One structure = one body. |  |  |
| torch-A | Noun | level 2 | light | a piece of wood [that is burning] |  |  |
| torture-A | Verb | level 2 |  | "hurt X [so X suffers much]" |  |  |
| trade-A | Verb | level 2 |  | "X trades Y for Z with A = X sells Y to A. and//or X buys Z from A" or "[A = X sells Y to A] [and//or X buys Z from A]" in subordinate clauses. |  |  |
| tradition-A | Noun | level 2 | custom |  |  |  |
| trample-A | Verb | level 2 | step on//crush |  |  |  |
| transgression-A | Noun | level 2 | crime |  |  |  |
| treasure-A | Noun | level 2 |  | Generic: “extremely valuable things _ generic _AorDsense”. Rule: “extremely valuable thing _genericOrFirst mention -> treasure” (Note: inherit number from “thing”) |  |  |
| treasurer-A | Noun | level 2 |  | "person [who manages money]" or pair with "manager", "official" or "servant" | treasurer |  |
| treasurer-A | Noun | level 2 |  | "Person [who is responsible for X's money]" | X's treasurer |  |
| treasury-A | Noun | level 2 |  | “room//building [that people put valuable things in]” |  | We have it, though I don’t think we need it |
| treasury-B | Noun | level 2 |  | “box [that people _generic put money [that was for the temple] into]” |  | We have it, though I don’t think we need it |
| tremble-A | Verb | level 2 | shake-C |  |  |  |
| troubled-A | Adjective | level 2 | upset//confused |  |  |  |
| troubled-A | Adjective | level 2 | upset//confused |  |  |  |
| trumpet-A | Noun | level 2 |  | "instrument//horn [that produces a loud sound [while//when X blows into instrument//horn]]", NOTE: use "X PLAYS an instrument//horn ... while/when X blows into..." |  |  |
| tumor-A | Noun | level 2 |  | "mass _inLDV of sick cells _inLDV" |  |  |
| tunnel-A | Noun | level 2 |  | "a long hole [that people//people-B//spirits are able [move through]]" |  |  |
| twin-A | Noun | level 2 |  | "2 people [who were birthed by the same mother at the same time]" (twins) or "1 of 2 people [who were birthed by the same mother at the same time]" (a twin) |  |  |
| twist-A | Verb | level 2 | squeeze//hit//tie |  |  |  |
| uncle-A | Noun | level 2 |  | “the brother of X’s father” or “the brother of X’s father or X’s mother” | X's uncle |  |
| uncle-B | Noun | level 2 |  | “the brother of X’s mother” | X's uncle |  |
| unrighteous-A | Adjective | level 2 | bad-B |  |  |  |
| urge-A | Verb | level 2 | tell//ask//encourage | “ask” for when a person needs to talk to a person of higher rank |  |  |
| value-A | Noun | level 1 |  |  |  |  |
| veterinarian-A | Noun | level 2 |  | “Doctor [who treats sick animals_generic]” |  |  |
| vine-A | Noun | level 2 |  | “plant of fruits/grapes]” Note: This rule should require “grapes” and not be used if the semantic representation just has "plant of fruits" |  |  |
| vinegar-A | Noun | level 2 |  | “sour liquid//wine” or pair with “wine” |  |  |
| vineyard-A | Noun | level 2 |  | “garden of grapes”. In the HE2, write "fruit/grapes", but the rule should only be implemented with "grapes". |  |  |
| viper-A | Noun | level 2 |  | “poisonous snake” |  |  |
| virgin-A | Noun | level 2 |  | “woman/girl/daughter [who never sexed a man]” |  |  |
| virgin-A | Noun | level 2 |  | “X never sexed a person” | X be a Virgin_man |  |
| virgin-A | Noun | level 2 |  | “X never sexed a man”. If there is ever a case where you want “sex a person” (probably not needed in the Bible), write that explicitly | X be a Virgin_woman |  |
| vision-A | Noun | level 2 | dream, picture | In some cases, you might be able to pair this with “dream” or "picture". In other cases, it may have to be expressed in a different way. |  |  |
| vomit-A | Verb | level 2 |  | “Y comes out from X’s stomach” | X vomits Y |  |
| vow-A | Noun | level 2 | promise |  |  |  |
| vow-A | Verb | level 2 | promise |  |  |  |
| vulture-A | Noun | level 2 |  | “big bird [that eats dead animals]” |  |  |
| wage-A | Noun | level 2 | money | Use pairing. Note: use number of “wage//wages” |  |  |
| wagon-A | Noun | level 2 | vehicle |  |  |  |
| wail-A | Verb | level 2 | cry//cry-out | “cry loudly” |  |  |
| wander-A | Verb | level 2 | walk or travel | “walk [without having a purpose]”. Previously we had "walk without a purpose", but I'm not sure that our senses of "without" work for that. |  |  |
| warrior-A | Noun | level 2 | soldier |  |  |  |
| weary-A | Adjective | level 2 | tired | it has been used in Malachi rather differently because paired with upset |  |  |
| weed-A | Noun | level 2 |  | “plant [that people do not want]” |  |  |
| weep-A | Verb | level 2 | cry |  |  |  |
| weight-A | Noun | level 2 |  | "an object [that has a certain weight-B] [and that X uses [in order to weigh a thing]]_optional" or in some circumstances you could pair that with "object" | meaning a particular weight used on a scale |  |
| welcome-A | Verb | level 2 |  | “Greet kindly” Or, depending on context, pair with “greet", "receive", or “accept-B” |  |  |
| well-A | Noun | level 2 |  | “deep hole [that water is in]” |  |  |
| whirlwind-A | Noun | level 2 | wind//storm |  |  |  |
| whisper-A | Verb | level 2 |  | “say-A very quietly” | whisper [" "] |  |
| whisper-B | Verb | level 2 |  | "say-B very quietly" | X whispers Y to Z |  |
| wholeheartedly-A | Adverb | level 2 | completely or much |  |  |  |
| wicked-A | Adjective | level 2 | evil |  |  | (but I don’t think we need it) |
| wickedly-A | Adverb | level 2 | badly-B |  |  |  |
| widow-A | Noun | level 2 |  | “woman [who had a husband [who died]]” |  |  |
| wilderness-A | Noun | level 2 | desert | Use the pairing desert/wilderness when it means an arid, uncultivated place with low population rather than a desert like the Sahara. |  |  |
| will-A | Noun | level 1 |  | Try to use “want_verb”. For instance: “thing [that X wants [to do]]” |  |  |
| winepress-A | Noun | level 2 |  | “place [where people _generic squeeze fruit/grapes _genericPlural [in-order-to make-E wine _generic]]” |  |  |
| wineskin-A | Noun | level 2 |  | “wine _genericGenitive container//bag of _madeOf leather” or pair with “container” |  |  |
| wink-A | Verb | level 2 |  | “X closes one of X's eyes for about a second” | X winks | It's not used often, but using the word would be so much better than the explication |
| winnow-A | Verb | level 2 |  | “separate covers of grain from X” | winnow X |  |
| wipe-A | Verb | level 2 | rub//clean |  |  |  |
| witch-A | Noun | level 2 |  | “woman [who uses magic]”. |  |  |
| witchcraft-A | Noun | level 2 | magic |  |  |  |
| wither-A | Verb | level 2 | die |  |  |  |
| wither-A | Verb | level 2 |  | "grass//flower//plant//crops become dry" | grass//flower//plant wither |  |
| witness-A | Noun | level 2 |  | "person//servant [who tells//tells/testifies about the things [that person//servant knows//sees//hears]]" |  |  |
| witness-A | Verb | level 2 | see or know or agree |  | x witnesses [ ] |  |
| witness-B | Verb | level 2 | see or know |  | X witnesses Y |  |
| wolf-A | Noun | level 2 |  | “violent//big wild dog” (TBTA currently uses "violent" for this explication - "jackal" is "wild dog") |  |  |
| womb-A | Noun | level 2 | body | "The place [that is inside a woman's body] [and that a baby is able [to be in]]". But in almost all cases, I think it would be better to pair it with "body". |  |  |
| wonder-A | Noun | level 2 |  | “things [that cause [people _generic to become very surprised/amazed]]”. Note: previously had “to be surprised/amazed”, but I think the new wording is better Another suggestion for “signs and wonders”: don’t use the noun “wonders”, but use instead “signs-B and great/wonderful actions [that X does through God's power-B]” which will be generated as “signs and wonderful miracles” (also see entry for “miracle”) |  |  |
| wonder-A | Verb | level 2 | think |  |  |  |
| wonderful-A | Adjective | level 2 | great |  |  |  |
| word-B | Noun | level 2 | message |  | "word" meaning God's revelation |  |
| work-out-A | Verb | level 3 |  |  |  |  |
| worker-A | Noun | level 2 |  | “person [who works]” |  |  |
| worker-A | Noun | level 2 |  | “person [who works for X]” | X’s worker |  |
| worship-A | Verb | level 2 | honor//praise//thank//love//serve |  |  |  |
| worthless-A | Adjective | level 2 |  | “X [who is not valuable]” or pair with “useless” or "bad-AorB" | worthless X |  |
| worthless-A | Adjective | level 2 |  | “be not valuable” Note: The rule for “worthless X” needs to be checked first | be worthless |  |
| worthy-A | Adjective | level 2 | good |  |  |  |
| wrath-A | Noun | level 2 | anger |  |  |  |
| wreath-A | Noun | level 2 |  | "circle of leaves" - in some cases can pair with “circle” |  |  |
| yeast-A | Noun | level 2 |  | “substance [that causes [bread to become big]]” |  |  |
| yoke-A | Noun | level 3 | pole-B//wood-B//load |  |  |  |
| zealous-A | Adjective | level 2 | loyal//faithful to X |  | zealous for X |  |

## Approved — pairing/explication ratified and added to the ontology

274 entries. Same usage as above; `approved` marks terms whose pairing/explication has been through review, so treat these as settled rather than provisional.

| Term | POS | Level | Paired with | Explication | Structure | Notes |
|---|---|---|---|---|---|---|
| account-A | Noun | level 1 |  | None needed – in the LDV |  |  |
| acknowledge-B | Verb | level 2 | accept//say |  | acknowledge [that something will happen] |  |
| ally-A | Verb | level 2 | join |  | ally with X |  |
| ancient-A | Adjective | level 2 |  | "extremely old" or pair with "old" |  |  |
| aqueduct-A | Noun | level 2 | stream |  | ESV conduit |  |
| archer-A | Noun | level 2 |  | "soldier [who uses a bow]" using the explication for "bow" |  |  |
| aroma-A | Noun | level 2 | smell |  |  |  |
| assemble-A | Verb | level 2 | gather |  |  |  |
| assembly-A | Noun | level 2 | group |  |  |  |
| associate-A | Verb | level 2 | Be with |  | associate with X |  |
| astonished-A | Adjective | level 2 |  | "extremely amazed" Note:  this will require a change in the rule for "amazed" that previously changed "extremely amazed" to just "amazed" |  |  |
| atone-A | Verb | level 2 | cover | Use only in literal alternates. In dynamics use "forgive". | atone for X |  |
| atonement-A | Noun | level 3 |  | You can use with "make-C" or "have-D". Include a simple alternate with "atone" and a dynamic alternate with "forgive" |  | yeah it's not that important I mean so you know the whole thing could be removed butit's okay doesn't matter |
| aunt-A | Noun | level 2 |  | “the sister of X’s father” or “the sister of X’s father or of X’s mother” | X's aunt |  |
| aunt-B | Noun | level 2 |  | “the sister of X’s mother” | X's aunt |  |
| balm-A | Noun | level 2 | oil//medicine |  |  |  |
| band-A | Noun | level 2 | rope |  | a narrow strip of leather or other material |  |
| bathe-A | Verb | level 2 |  | "X bathes = X washes X's body" | X bathes |  |
| beat-D | Verb | level 1 |  | The beating of a heart |  |  |
| behavior-A | Noun | level 1 |  | None needed – in the LDV |  |  |
| bell-A | Noun | level 1 |  | in LDV | Meaning: a metal usually cup shaped object that rings or clangs when you strike or shake it |  |
| beneficial-A | Adjective | level 2 | helpful (in LDV) |  |  |  |
| boast-D | Verb | level 2 |  | "proudly-A say, ["..." with direct quote | X boasts, "..." |  |
| brier-A | Noun | level 2 |  | "plant [that has sharp points] [and that grows over other things]" |  |  |
| brilliant-A | Adjective | level 2 |  | Suggestion: use “very bright/brilliant” (We can add a theta grid rule to change “very brilliant” to just “brilliant”) |  |  |
| bring-D | Verb | level 1 |  |  | for use with abstract patients |  |
| broken-A | Adjective | level 2 |  | "X [that broke-D]" or “X that Y broke” (If you need Y, block the rule) | broken X |  |
| broom-A | Noun | level 2 | brush |  |  |  |
| brush-A | Noun | level 1 |  |  |  |  |
| burden-A | Noun | level 2 | load//trouble |  |  |  |
| buttock-A | Noun | level 1 |  |  |  |  |
| cart-A | Noun | level 2 | vehicle |  |  |  |
| cast-out-A | Verb | level 2 |  | “force [X to leave Y]”, where “X = spirit-B or demon” only. If “Y” is omitted (because it is implicit and gets removed), the rule can generate just “cast out X”. | X casts out Z from Y |  |
| cell-A | Noun | level 1 |  |  | means "the smallest part of a living thing that can exist independently" |  |
| chain-A | Verb | level 2 |  | "tie with chains" |  |  |
| chase-B | Verb | level 1 |  | to catch (but not hurt) |  |  |
| chop-A | Verb | level 2 | cut |  |  |  |
| cleverly-A | Adverb | level 1 |  |  |  |  |
| cloak-A | Noun | level 2 | coat |  |  |  |
| coal-B | Noun | level 1 |  |  | meaning "a piece of wood or coal that is hot because it was burning" |  |
| cobra-A | Noun | level 2 |  | “poisonous snake [that has a flat head]” |  |  |
| collapse-A | Verb | level 2 | fall-E | Or try to use "be destroyed" |  |  |
| comfortably-A | Adverb | level 1 |  |  |  |  |
| conceal-A | Verb | level 2 | hide |  |  |  |
| consider-how-A | Verb | level 1 |  |  | consider-how [something happens] |  |
| constantly-A | Adverb | level 2 | continuously |  |  |  |
| consume-A | Verb | level 2 | destroy//take-away |  | Note: this is not about eating |  |
| continuous-A | Adjective | level 1 |  | In the LDV, use it |  |  |
| cord-A | Noun | level 2 |  | “thin ropes” |  |  |
| cord-A | Noun | level 2 |  | ‘thin rope’ or pair with "rope" or "string" |  |  |
| counsel-A | Noun | level 2 | advice |  |  |  |
| counsel-A | Verb | level 2 | advise |  |  |  |
| counselor-A | Noun | level 2 |  | "person [who advises//counsels X]" |  |  |
| crafty-A | Adjective | level 2 | clever |  | Note: crafty has a negative connotation of cleverness for selfish reasons |  |
| cross-B | Verb | level 1 |  | To go from one side of a thing to the other side |  |  |
| crouch-A | Verb | level 2 | kneel |  |  |  |
| curds-A | Noun | level 2 |  | "thick substance [that forms in sour milk]" |  |  |
| curse-A | Noun | level 2 | punishment |  |  |  |
| cursed-A | Adjective | level 3 |  | Normally use in a complex alternate with a simple alternate using the verb form. |  |  |
| decrease-A | Verb | level 1 |  |  |  |  |
| decree-A | Verb | level 2 | order | Note to P2: use a patient argument for “decree” instead of a destination argument so it can be paired with “order” |  |  |
| defect-A | Noun | level 2 | problem//injury//wound | "physical problem" or pair with "problem//injury//wound" |  |  |
| den-A | Noun | level 2 | hole | "hole [that X lives in]" or pair with "hole" |  |  |
| depth-A | Noun | level 2 |  | “deep place” |  |  |
| devote-A | Verb | level 2 | Give |  |  |  |
| discern-A | Verb | level 2 | recognize//know//examine |  | discern X(noun) |  |
| discharge-A | Noun | level 2 |  | "liquid [that comes//flows from X's body] [and that (implicit-situational) is not normal]" with the implicit clause optional |  |  |
| disgusting-A | Adjective | level 2 |  | “very (extremely?) bad (not morally)” |  |  |
| dishonest-A | Adjective | level 2 |  | “X [that is not honest]” | dishonest X |  |
| dishonest-A | Adjective | level 2 |  | “are not honest” - Note: check rule for dishonest X first | X is dishonest |  |
| dread-A | Noun | level 2 | fear _inLDV |  |  |  |
| drip-A | Verb | level 2 | fall |  |  |  |
| dye-A | Noun | level 2 |  | "liquid [that is put by people _possiblyImplicit on X [so that X will have color]]" or in some circumstances you might pair with "liquid" or "color" |  |  |
| emphasize-A | Verb | level 2 |  | “Say strongly [that …]” | emphasize [that... ] |  |
| enable-B | Verb | level 2 |  | “cause [X to be able-B [to Y]]”, or pair with “help-B” | enable [X to Y] |  |
| entire-A | Adjective | level 2 | Whole |  |  |  |
| equip-A | Verb | level 2 | Supply (in the LDV) |  |  |  |
| especially-A | Adverb | level 1 |  |  |  |  |
| everywhere-A | Adverb | level 1 |  | Not needed – in the LDV |  |  |
| evil-A | Noun | level 3 |  | Simple alternate could use “evil_adj” |  |  |
| excuse-A | Verb | level 1 |  |  |  |  |
| excuse-A | Noun | level 1 |  |  |  |  |
| exile-A | Noun | level 2 |  | “person [who was previously taken from X _optional to Y by Z]” OR “person [that was forced by Z _optionallyImplicit [to go from X _optional to Y]]” or pair with "take//captured" | an exile |  |
| expert-A | Noun | level 2 |  | “Person who knows X well”. The issue here is that we might want to use man or some other noun instead of person. If so, we should use the explication explicitly | expert of X |  |
| express-A | Verb | level 1 |  |  | express X, where X is a thought or feeling |  |
| fabric-A | Noun | level 2 | cloth-A//cloth-B |  | means cloth material |  |
| fact-A | Noun | level 1 |  | Not needed – in the LDV |  |  |
| fasten-A | Verb | level 2 | tie |  |  |  |
| favor-A | Noun | level 3 |  |  |  |  |
| fiery-A | Adjective | level 2 | much//strong |  |  |  |
| fin-A | Noun | level 2 | fish//part |  |  |  |
| firm-A | Adjective | level 2 | Strongly |  |  |  |
| firmly-A | Adverb | level 2 | Strongly |  |  |  |
| flame-A | Noun | level 1 |  |  |  |  |
| flash-A | Verb | level 2 | shine-B |  |  |  |
| flesh-B | Noun | level 3 |  | Using a complex alternate, or you might pair with "body", depending on the circumstance. | Meaning the sinful human nature |  |
| flint-A | Noun | level 2 | stone-B |  | the material |  |
| flow-A | Noun | level 1 |  |  | Meaning movement of liquid or air |  |
| forcefully-A | Adverb | level 2 | strongly |  |  |  |
| form-A | Verb | level 1 |  |  | Definition: to start to exist, especially by natural processes |  |
| fortress-A | Noun | level 2 |  | “building [that has strong-A walls]” |  |  |
| fountain-A | Noun | level 2 |  | “Structure [that water comes from]” - Consider also if “spring” might be appropriate |  |  |
| frequently-A | Adverb | level 2 | Often |  |  |  |
| fuel-A | Noun | level 2 | thing-A |  |  |  |
| funeral-A | Noun | level 1 |  |  |  |  |
| furthermore-A | Adverb | level 2 | also |  |  |  |
| gesture-A | Verb | level 2 | move X |  | gesture with X |  |
| glutton-A | Noun | level 2 |  | “person [who eats too//extremely much food]” |  |  |
| glutton-A | Verbal phrase | level 2 |  | “X eats too//extremely much food” - rule after rule for just "glutton" | X be glutton |  |
| godless-A | Adjective | level 2 |  | "X [who ignore God]" | godless X |  |
| godless-A | Adjective | level 2 |  | "X ignores God". Note: This rule needs to be checked after the one for "godless X" | X be godless |  |
| government-B | Noun | level 2 | rule-B |  | the process of governing |  |
| grandparent-A | Noun | level 2 |  | “Parent of the parent of a child”. “X’s grandparent = parent of X’s parent” |  |  |
| graze-A | Verb | level 2 |  | "eat grass" |  |  |
| greetings-A | Noun | level 1 |  |  |  |  |
| growl-A | Verb | level 2 |  | "make-C an angry sound" or for an animal, pair with "shout-C" |  |  |
| grumble-A | Verb | level 2 | complain |  |  |  |
| hand-over-A | Verb | level 2 |  | Suggestion: use something like "put something in X's hands" | hand-over something to X |  |
| harsh-A | Adjective | level 2 | cruel//angry |  |  |  |
| harvest-A | Noun | level 2 |  | "the time [that people harvest crops at]" |  |  |
| harvest-A | Noun | level 2 |  | "the time [that people harvest wheat//barley//etc at]" | Harvest of X (X harvest) |  |
| harvest-B | Noun | level 2 |  | X [that people gathered-B//got//grew//harvested] |  |  |
| hedge-A | Noun | level 2 |  | “row of bushes” or pair with "bush" |  |  |
| hedgehog-A | Noun | level 2 |  | "small animal [that is covered by hard sharp hairs-B]" |  |  |
| help-A | Noun | level 1 |  |  |  |  |
| hen-A | Noun | level 2 |  | "female chicken" |  |  |
| horrified-A | Adjective | level 2 | afraid//upset |  |  |  |
| horror-A | Noun | level 2 | fear (in LDV) |  |  |  |
| horseman-A | Noun | level 2 |  | "man//person [who rides a horse]" |  |  |
| household-A | Noun | level 2 |  | "people [who live in X's house]" using "live-A" (dwell), or could pair with "family" or "people". But be careful. If the meaning is better expressed by "family" (meaning long-term descendents), use "family". | X's household |  |
| hyena-A | Noun | level 2 |  | "wild animal [that eats dead animals] [and that makes a sound [that is like laughter]]" |  |  |
| image-B | Noun | level 2 | object | This is for an object honoring something like a king or god, of which the shape is not known. Previously had "object//model [that has//is the shape/form of X]", but that meaning is the same as "statue". For a meaning where it's not clear what the shape of the object was, use "object/image-B"  or just "object" |  |  |
| impurely-A | Adverb | level 2 | badly_morally |  |  |  |
| incite-A | Verb | level 2 | cause |  |  |  |
| indignant-A | Adjective | level 2 | angry//upset | Use “angry” |  |  |
| infected-A | Adjective | level 1 |  |  |  |  |
| initially-A | Adverb | level 2 | previously |  |  |  |
| insane-A | Adjective | level 2 | crazy |  |  |  |
| inspire-B | Verb | level 2 | cause-A//teach |  | inspire [X to Y] |  |
| intend-A | Verb | level 2 | plan//want |  |  |  |
| itch-A | Verb | level 2 |  | "want to scratch//(rub with X's nails) X's skin" (using explication for "scratch") |  |  |
| Jubilee-A | Noun | level 4 |  |  | ( restoration) as in "year of Jubilee" |  |
| judgment-A | Noun | level 2 | decision |  | A specific judgment(=decision) | Even though it is in the LDV |
| judgment-B | Noun | level 3 |  | Note: This is the process of judgment; normally include a sample alternate | The process of judgment |  |
| knit-A | Verb | level 2 | make |  |  |  |
| laughter-A | Noun | level 1 |  |  |  |  |
| Levite-A | Noun | level 2 |  | "men//people of Levi-B _tribe" or “men//people [who are in the tribe named Levi-B]”. If you want to emphasize some aspect of the Levites' role, add a restrictive thing modifying clause like "[(implicit-situational) who helped the priests]". also "people of the family-B//clan named X" | (and other -ites; these may not be words in the ontology, but different expressions in English of the explication) |  |
| limit-A | Noun | level 1 |  |  |  |  |
| long-B | Verb | level 2 | want |  | long [for something to happen] |  |
| long-C | Verb | level 2 | want |  | long for noun |  |
| luxuriously-A | Adverb | level 2 | comfortably//well |  |  |  |
| majesty-A | Noun | level 3 |  |  |  |  |
| mass-A | Noun | level 1 |  |  | means "an amount of a substance that does not have a definite or regular shape" |  |
| material-A | Noun | level 2 | thing-A |  | means: the things that are used for making or doing something |  |
| matter-A | Noun | level 1 |  | Not needed – in the LDV | meaning "a subject or situation that you have to think about or deal with" |  |
| mercifully-A | Adverb | level 2 | kindly |  |  |  |
| mildew-A | Noun | level 2 | disease |  |  |  |
| ministry-A | Noun | level 2 | work |  |  |  |
| monument-A | Noun | level 2 | structure |  |  |  |
| mortal-A | Noun | level 2 |  | "person [who will eventually die]" or pair with something like "person" |  |  |
| natural-A | Adjective | level 1 |  |  |  |  |
| naturally-A | Adverb | level 1 |  | Note: adverb form of "natural" in the LDV |  |  |
| offering-B | Noun | level 2 | gift | offering = gift to a god//Baal//Asherah |  | Do we need a separate word? |
| offspring-A | Noun | level 2 | children |  |  |  |
| ostrich-A | Noun | level 2 |  | "big bird [that runs quickly] [but that is not able [to fly]]" |  |  |
| owl-A | Noun | level 2 |  | "bird [that has big eyes] [and that hunts at night]" |  |  |
| pair-A | Noun | level 2 |  | "group of 2 X" | "pair of X" |  |
| parched-A | Adjective | level 2 | dry |  |  |  |
| peg-A | Noun | level 2 | stick//nail |  |  |  |
| penalty-A | Noun | level 2 | price |  |  |  |
| permanent-A | Adjective | level 1 |  |  |  |  |
| permit-A | Verb | level 2 | allow |  |  |  |
| plaster-A | Noun | level 2 |  | "thick substance [that is used by X _optionallyImplicit [in order to cover walls]]" |  |  |
| pledge-A | Noun | level 2 |  | "a thing that X gives//offers to Y [in order to show Y [X will return a thing to Y]]" or "sign of a promise" | meaning collateral or "security" in the Bible |  |
| plunder-A | Noun | level 2 | thing-S//money//wealth | "things [that X takes from X's enemies]" |  |  |
| potter-A | Noun | level 2 |  | “person [who makes pots with clay]” |  |  |
| powder-A | Noun | level 1 |  |  |  |  |
| practice-A | Noun | level 2 | thing-B//action |  |  |  |
| prey-A | Noun | level 2 |  | "animal [that X hunts [in order to eat animal]_optional ]" | X's prey |  |
| profane-A | Verb | level 2 |  | "treat X [as-though X was not special/holy]" | profane X |  |
| pump-A | Verb | level 1 |  |  | pump X_optional |  |
| purely-B | Adverb | level 2 | well-B |  |  |  |
| purify-A | Verb | level 2 |  | “religiously clean X” |  |  |
| quiver-A | Noun | level 2 |  | "bag//container of arrows" using the explication for arrows or pair with "bag" or "container" or use in complex alternate |  |  |
| rarely-A | Adverb | level 1 |  |  |  |  |
| ravine-A | Noun | level 2 | valley |  |  |  |
| razor-A | Noun | level 2 | blade |  |  |  |
| really-A | Adverb | level 1 |  | in the LDV, or could use "actually" |  |  |
| reap-A | Verb | level 2 | gather |  |  |  |
| record-A | Verb | level 1 |  |  |  |  |
| recover-A | Verb | level 2 |  | “Become healthy again” |  |  |
| refined-A | Adjective | level 2 | rich//gentle//kind |  |  |  |
| related-A | Adjective | level 1 |  | in the LDV |  |  |
| repay-A | Verb | level 2 | return-E//punish//pay |  |  |  |
| reservoir-A | Noun | level 2 | pool |  |  |  |
| restore-B | Verb | level 2 |  | "cause X to become stong-A//strong-C again" or pair with "help" | restore a person |  |
| revolt-A | Noun | level 3 |  | Suggestion: use in a complex alternate, with a simple alternate using "rebel". |  |  |
| rob-A | Verb | level 1 |  |  | X robs Y |  |
| rue-A | Noun | level 2 | null |  | an herb that tastes bitter |  |
| rug-A | Noun | level 2 | cloth |  |  |  |
| ruined-A | Adjective | level 2 | bad-A (not morally)//empty |  |  |  |
| rule-B | Noun | level 1 |  |  | the process of ruling |  |
| sanctuary-A | Noun | level 2 |  | "holy place" (write "special/holy place" in He2, but this rule should only be activated if "holy" is also available - because "special place" is too general.  If you want to generate "holy place", block the rule for "sanctuary".) |  |  |
| sanctuary-B | Noun | level 2 |  | "sacred place" for worship of gods (write "special//religious/holy place" in He2, but this rule should only be activated if "sacred" is also available.  If you want to generate "sacred place", block the rule for "sanctuary-B".) |  |  |
| sash-A | Noun | level 2 |  | "belt of(made-of) cloth" generated as "cloth belt" if we don't have the complex word |  |  |
| scale-B | Noun | level 2 | fish//part |  |  |  |
| scorch-A | Verb | level 2 | burn//destroy//harm |  |  |  |
| scratch-A | Verb | level 2 |  | "rub with nails" (fingernails) |  |  |
| senseless-A | Adjective | level 2 | Stupid |  |  |  |
| serious-A | Adjective | level 1 |  |  |  |  |
| seriously-A | Adverb | level 1 |  |  |  |  |
| settle-A | Verb | level 2 |  | "start to live" |  |  |
| severe-A | Adjective | level 2 | bad-A//big//angry |  |  |  |
| severely-A | Adverb | level 2 | much |  |  |  |
| shame-A | Verb | level 2 |  | “Cause [X to become//be//feel ashamed-A]” |  |  |
| shameful-A | Adjective | level 2 | bad_morally |  |  |  |
| shamefully-A | Adverb | level 2 | badly-B |  |  |  |
| share-A | Noun | level 2 | part |  |  |  |
| sharpen-A | Verb | level 2 |  | "cause [X to be//become sharp]" | sharpen X |  |
| sheet-B | Noun | level 1 |  |  | Meaning a thin flat piece of something like metal |  |
| shoot-A | Noun | level 2 | branch//plant |  |  |  |
| shrewd-A | Adjective | level 2 | clever |  |  |  |
| shrewdly-A | Adverb | level 2 | cleverly |  |  |  |
| situation-A | Noun | level 1 |  |  | meaning: "the things that are happening and all the conditions that exist at a particular time in a particular place" |  |
| slippery-A | Adjective | level 1 |  |  |  |  |
| smash-A | Verb | level 2 | break |  |  |  |
| sow-A | Verb | level 2 | plant |  |  |  |
| spade-A | Noun | level 1 |  |  |  |  |
| spit-B | Verb | level 1 |  |  | to spit something other than saliva out of one's mouth (spit-A is for saliva) |  |
| splendor-A | Noun | level 3 |  |  |  |  |
| sport-A | Noun | level 1 |  |  |  | yeah  I did the same thingI don't know why when I looked there wasn't anything there so I put it but |
| spot-A | Noun | level 1 |  |  | meaning "a usually round area that is different from the surrounding area" |  |
| stand-A | Noun | level 2 | table |  | for holding a lamp |  |
| statement-A | Noun | level 1 |  | It’s in the LDV, but consider if “words” would be satisfactory |  |  |
| stick-A | Verb | level 1 |  |  | (intransitive) X sticks to Y (optional?) |  |
| stray-A | Verb | level 2 | leave X |  | X strays from Y |  |
| stretch-B | Verb | level 1 |  |  | X stretches Y ( transitive) |  |
| strictly-A | Adverb | level 1 |  |  |  |  |
| stronghold-A | Noun | level 2 |  | "strong place" or "safe place" - also see "refuge" |  |  |
| strongly-A | Adverb | level 1 |  |  |  |  |
| stubble-A | Noun | level 2 |  | "the dry parts [that stay [after the crops of a field are collected//harvested by people _possiblyImplicit]] of plants" |  |  |
| stump-A | Noun | level 2 | bottom-B |  |  |  |
| subject-A | Noun | level 1 |  | Not needed – in the LDV |  |  |
| succeed-B | Verb | level 2 | replace |  | succeed X, meaning to come after, or to replace X |  |
| sure-A | Adjective | level 1 |  |  | sure [something will happen] |  |
| sustain-A | Verb | level 2 | help//support |  |  |  |
| sweep-away-A | Verb | level 2 | take-away//destroy |  |  |  |
| tambourine-A | Noun | level 2 |  | "instrument that produces sound [when X shakes instrument]" |  |  |
| tempt-B | Verb | level 2 | tell-B |  | tempt [X to Y] |  |
| tent-of-meeting-A | Noun | level 2 |  | "tent [that Yahweh meets X in//at]" - As a default, we recommend X = “Yahweh’s people”, but X may be different for specialized purposes, like "tent [that Yahweh met Moses in//at]". |  |  |
| terrified-A | Adjective | level 2 |  | “extremely afraid” |  |  |
| territory-A | Noun | level 2 | land//country |  |  |  |
| threat-A | Noun | level 2 | danger |  |  |  |
| tongs-A | Noun | level 2 | tool |  |  |  |
| tooth-B | Noun | level 1 |  |  | of a saw or similar object |  |
| trim-A | Verb | level 2 | cut |  | meaning to cut parts off of something |  |
| trouble-A | Verb | level 2 |  | “cause [X to have trouble]” | trouble X |  |
| tunic-A | Noun | level 2 |  | Suggestion: use something like "long shirt" |  |  |
| unfaithful-A | Adjective | level 2 |  | “X [who is not faithful]” | Unfaithful X |  |
| unfaithful-A | Adjective | level 2 |  | “not be faithful” - Note: the rule for “unfaithful X’ should be implemented first | Be Unfaithful |  |
| urgent-A | Adjective | level 1 |  | Not needed-in the LDV |  |  |
| usefully-A | Adverb | level 1 |  |  |  |  |
| various-A | Adjective | level 2 | different//many |  |  |  |
| victim-A | Noun | level 2 | person |  |  |  |
| vindicate-A | Verb | level 2 |  | "prove [that X is right]" | vindicate X |  |
| watchman-A | Noun | level 2 |  | "person//man [who watches X]" or "who looks" |  |  |
| water-B | Noun | level 2 | sea, lake, stream, or river |  |  |  |
| weave-A | Verb | level 2 | make | cross threads [in order to make cloth] |  |  |
| weight-B | Noun | level 1 |  |  | meaning how heavy something is |  |
| whisper-C | Verb | level 2 |  | "speak very quietly" | X whispers about Y to Z |  |
| worry-A | Noun | level 2 |  | "things-B [that cause [people _generic to worry]]" |  |  |
| writhe-A | Verb | level 2 | turn//move |  |  |  |
| writing-A | Noun | level 2 | message |  |  |  |
| yoke-A | Verb | level 2 |  | “attach X to Y with a pole-B/yoke” (I suggest “load” instead of “pole” - Richard: I don’t like that. The yoke here is to attach animals to each other. “Load” is OK for the entry above depending on the context.) | Yoke X to Y |  |

## Suggested — proposed but not yet ratified

Only 6 entries. Treat these as a starting point, not a confirmed fix — verify against `/simplification_hints` before relying on one, since the sheet itself doesn't yet mark them settled.

| Term | POS | Level | Paired with | Explication | Structure | Notes |
|---|---|---|---|---|---|---|
| crane | Noun | level 2 |  | Suggestion:  tall bird [that has a long neck and long thin legs] |  |  |
| exchange | Verb | level 1 |  | In LDV; used 18 times and used before in TBTA.  Not in Ontology. |  | No but needs mentioning? |
| fault | Noun | n/a | wrong <thing> | Use completely or something like that | without fault |  |
| grasp | Verb | level 2 |  | suggestion: hold/grasp |  | has been used before |
| mighty | Adjective | n/a | strong | Use "powerful" |  |  |
| swift | Noun | level 2 |  | Suggestion: bird [that flies all of the time] [and that cry-out/screams loudly] |  |  |

## Not used — not an ontology entry at all

354 entries, level `n/a`. These words are not in the ontology under any level — there is nothing to pair with in the `simple/complex` sense. Where a `Paired with` or `Explication` value is given, treat it as a direct substitution (the recommended replacement word or phrase), not a slash-notation pairing.

| Term | POS | Level | Paired with | Explication | Structure | Notes |
|---|---|---|---|---|---|---|
| : | Punctuation | n/a | . |  |  | though Richard would like it |
| abyss | Noun | n/a |  | We have been using "extremely deep hole/pit" with a footnote when it first occurs in a book |  |  |
| accurate | Adjective | n/a |  | Use "correct" |  | Previously I put "Yes", but I think we can just use "correct". It's only used four times in the Bible. |
| addicted | Adjective | n/a |  | Suggestion: use explicitly “X is not able to stop doing Y” |  |  |
| admonish | Verb | n/a |  |  |  |  |
| adversary | Noun | n/a |  | Suggestion: enemy |  |  |
| afflict | Verb | n/a |  | Try to use "oppress" or "suffer" or "cause" or "cause to suffer" |  |  |
| against | Adposition | n/a |  | For opposition, normally use "oppose"; use "against-A" for being against in the sense of beside or next to, like in "lean against" |  |  |
| alcoholic | Noun | n/a |  | “Person [who drinks too much alcohol//wine]” OR “person [who always//often becomes drunk]” | be an alcoholic |  |
| all-the-time | Phrase | n/a |  | Use “Always” |  |  |
| amazing | Adjective | n/a |  | We could consider adding it to be paired with something like “good”, but for now I recommend trying to use “surprised/amazed” or “surprise/amaze”. |  |  |
| antichrist | Noun | n/a |  | Suggestion: use "enemy of Christ" |  |  |
| anxiety | Noun | n/a |  | Try to use the verb "worry". |  |  |
| appetite | Noun | n/a |  | Suggestion: use something like “want to eat food_implicit” or “hungry” or “things that they want/desire” |  |  |
| argumentative | Adjective | n/a |  | Suggestion: “routinely argue much with people” | be argumentative with X |  |
| article | Noun | n/a |  | Use “thing” |  |  |
| as | Adposition | n/a |  | Sometimes use "just like" |  |  |
| as-a-result | Phrase | n/a |  | Use “then” or “thus” or “because of these things” or "because..." |  |  |
| ascribe | Verb | n/a |  | Use "give" or "say that..." with adjectives |  |  |
| assume | Verb | n/a |  | Suggestion: use “think” |  |  |
| at-the-same-time | Phrase | n/a |  | Use “also” or some other construction |  |  |
| awl | Noun | n/a |  | Suggestion: "tool [that has a sharp point]" |  |  |
| backbone | Noun | n/a |  | Suggestion: Use "bone of back" |  |  |
| banquet | Noun | n/a |  | We could consider adding this as a complex word, but I think that "feast" would probably be sufficient. |  |  |
| barbarian | Noun | n/a |  | Suggestion for the New Testament: “wild person [who (implicit-situational) does not know Greek]” |  |  |
| barracks | Noun | n/a |  | One possibility is “military building” |  |  |
| barrel | Noun | n/a |  | “wood container” |  | not for now |
| barren | Adjective | n/a |  | Suggestion: "woman [who is not able-A [to have children]]" | barren woman |  |
| bat | Noun | n/a |  | Suggestion: "animal [that has wings [that are like leather]] [and that flies at night]" -- but in many cases such an involved explication would be distracting |  |  |
| be out-of-control | Verbal Phrase | n/a |  | Suggestion: “not control himself” |  |  |
| be-in-good-spirits | Phrase | n/a |  | Suggestion: Use “be happy/cheerful” |  |  |
| be-possessed | Verb | n/a |  | Use “control”. We have a collocation rule that changes to “possessed”. | be Possessed by a demon//spirit//Beelzebub//Satan |  |
| bear | Verb | n/a |  | Use “birth children” or “have a child inside her” or something like that depending on the context | bear children |  |
| bear | Verb | n/a |  | “be patient with people [even if people annoy you]” | bear with people |  |
| blasphemy | Noun | n/a |  | Use “blaspheme” |  |  |
| bless-food | Phrase | n/a |  | Suggestion: "thank God for the food” |  |  |
| blight | Noun | n/a |  | Suggestion: use "plants wither" |  |  |
| boundary | Noun | n/a |  | Use “border” |  |  |
| breastfeed | Verb | n/a |  | See entry for “nurse” |  |  |
| broom-tree-or-bush | Noun | n/a |  | Suggestion: use "desert bush" |  |  |
| by-means-of | Adposition | n/a |  | Suggestion: use “by using” or “because of” or some other construction |  |  |
| cavalry | Noun | n/a |  | Use "horsemen" |  |  |
| cease | Verb | n/a |  | Use “stop Xing” for the phase 1. Then the “stop” will be converted to the cessative feature | cease Xing |  |
| census | Noun | n/a |  | Use “count” |  |  |
| certain | Adjective | n/a |  | Use "sure" | meaning "sure" |  |
| certify | Verb | n/a |  |  |  |  |
| charity | Noun | n/a |  | “give money or other things to poor people” | do charity |  |
| cheerful | Adjective | n/a |  | Suggestion: use “happy” |  |  |
| cherish | Verb | n/a |  | Suggestion:“think/consider/realize/know [that X is very valuable]” or “Want X [just like you want a thing [that is very valuable]]” | cherish X |  |
| circumcised-heart | Phrase | n/a |  | We used: “(literal) You(people) are not willing [to allow [God _implicitNecessary to change/circumcise your(people's) hearts]]. (dynamic) Your(people's) hearts are not good-B.” |  |  |
| citadel | Noun | n/a |  | Use “fortress” |  |  |
| colonnade | Noun | n/a |  | Suggestion: "porch [that had posts/beams and a roof]" |  |  |
| communicate | Verb | n/a |  | Suggestion: use “tell” or “say” | communicate X(plan/message) |  |
| compassionate | Adjective | n/a |  | Suggestion: “care for people [who are suffering]” {} consider using 'kind//merciful' | be compassionate |  |
| conceited | Adjective | n/a |  | Use "proud-A" |  |  |
| conceive | Verb | n/a |  | For just "X conceived", consider using "X became pregnant". For "X conceived Y", consider "Y became alive inside X's womb" |  | not for now |
| confirm | Verb | n/a |  | Suggestion: “show-B Y [X is true]” | confirm X (to Y) |  |
| contempt | Noun | n/a |  | Suggestion: something like "X does not respect Y" or "X shows [that X does not respect Y]" |  |  |
| continual | Adjective | n/a |  | Use "continuous" |  |  |
| continually | Adverb | n/a |  | Use "continuously" or "continues to ..." |  |  |
| convince | Verb | n/a |  | Use “persuade” |  |  |
| cormorant | Noun | n/a |  | Suggestion: "big black bird of the sea" |  |  |
| craftsman | Noun | n/a |  | Consider using something like "person [who is able [to skillfully make things]]" |  | not for now |
| crave | Verb | n/a |  | Suggestion: Use “very much want” |  |  |
| Cretan | Noun | n/a |  | suggestion: Person of Crete |  |  |
| crimson | Adjective | n/a |  | Suggestion: something like "dark red" |  |  |
| crooked | Adjective | n/a |  | Use “not straight” | crooked paths |  |
| crucible | Noun | n/a |  | Suggestion: Use “furnace” or just “fire” |  |  |
| crystal | Noun | n/a |  | Suggestion: use something like "clear stone-B". |  |  |
| cucumber | Noun | n/a |  | Suggestion: use something like 'long green vegetable' or 'a long green vegetable [that contains much-many water]' |  |  |
| cunning | Adjective | n/a |  | Use "crafty" |  |  |
| cure-A | Verb | level 2 |  |  | means to heal | This word is not in the LDV - since it is not simple it is likely not needed since we already have "heal" |
| curse-oneself | Verb | n/a |  | Consider a direct quote, depending on context. For example: X said, “I pray-hope God punishes me if I am not telling the truth.” | X curses X |  |
| dawn | Verb | n/a |  | Use “sun rises” | (day) dawns |  |
| day-of-judgment | Phrase | n/a |  | Use “the day [that God will judge all the people of the earth _optional on]” |  |  |
| day-of-judgment | Phrase | n/a |  | Use “the day [that God will judge all the people of the earth on]]” |  |  |
| dear | Adjective | n/a |  | Use “whom X love” | dear X (attributive, indicating affection) |  |
| delighted | Adjective | n/a |  | Suggestion: "very pleased" |  |  |
| deliver | Verb | n/a |  | Use “save” |  |  |
| descended-from | Adjective | n/a |  | Use “descendent” or “In the family of” |  |  |
| despair | Verb | n/a |  | Suggestion: "X does not have hope" | X despairs |  |
| dignity | Noun | n/a |  | Maybe use “honor” - see the Longman dictionary entry |  |  |
| diligent | Adjective | n/a |  | Suggestion: Use “works hard” |  |  |
| disappear | Verb | n/a |  | Suggestion: Use something like “people suddenly stopped seeing X” |  |  |
| discipline | Noun | n/a |  | Suggestion: Try to use a verb, correct or rebuke or discipline. Or use the noun 'instruction' |  | no for now |
| disobedient | Adjective | n/a |  | Suggestion: use the verb “not obey” | be disobedient |  |
| dispute | Verb | n/a |  | Use “argue” or “quarrel” |  |  |
| disrespectful | Adjective | n/a |  | “X says//does bad-B things [that show [X does not respect Y]]” | X be disrespectful to Y |  |
| do-your-best | Phrase | n/a |  | “Try very hard” |  |  |
| doctrine | Noun | n/a |  | Suggestion: use "teaching" |  |  |
| doe | Noun | n/a |  | Suggestion: use "female animal/deer" or just "animal/deer" |  |  |
| draw | Verb | n/a |  | Use get//pull-out | draw water/sword |  |
| drive-out | Verb | n/a |  | See “Cast-out” | drive-out X from Y |  |
| drunkard | Noun | n/a |  | “Person [who drinks too much alcohol//wine]” or “person [who always//often becomes drunk]” or "person [who is often drunk]" |  |  |
| dusk | Noun | n/a |  | Use “twilight” |  |  |
| ear-lobe | Noun | n/a |  |  |  |  |
| effort | Noun | n/a |  | Use "try hard" | make every effort |  |
| elect | Noun | n/a |  | Suggestion: “the people [whom the Lord-A chose-B [to be the Lord's-A people]]” | (the) elect |  |
| embrace | Verb | n/a |  | This could be made a complex term, but I suggest that we use “hug”. |  | no for now |
| emerald | Noun | n/a |  | Suggestion: "use something like "valuable/precious green stone" |  |  |
| envoy | Noun | n/a |  | Use “messenger = person [who takes messages to people]” |  |  |
| epileptic | Adjective | n/a |  | Suggestion: “X sometimes _optional is not able [to control X’s body]]” | X is eplieptic | (I had written to add this, but I don't see the need. Communicate with Richard if there seems to be a need for this.) |
| esteem | Verb | n/a |  | Use “respect” |  |  |
| everlasting | Adjective | n/a |  | Suggestion: use forever_adverb (like “everlasting life” -> “life that we have forever”) |  |  |
| evildoer | Noun | n/a |  | Suggestion: “person [who does evil things]”. |  |  |
| excrement-A | Noun | n/a |  | Use "dung" |  |  |
| exhort | Verb | n/a |  | Use something like "tell" or "say" |  |  |
| exile | Noun | n/a |  | Use the verb instead | exile (event) |  |
| extol | Verb | n/a |  | Suggestion: use "praise much" |  |  |
| falcon | Noun | n/a |  | Suggestion: "bird [that hunts animals] [and that flies quickly]" |  |  |
| false-disciple | Phrase | n/a |  | Suggestion: “person [who does not truly follow _routinely X]”; NOTE: You must ask P2 to block the rule for “X’s disciple” |  |  |
| false-prophet | Noun | n/a |  | "person [who tells false messages [that are not from God] to people]" using "be-T" (Note: we used to have "person [who tells false messages [that do not come from God] to people]", but we shouldn't use "come", especially "come-A", in this context. So there may need to be corrections to our semantic representations.) |  |  |
| false-teacher | Noun | n/a |  | Use "person [who teaches false things-C]" |  |  |
| false-witness | Noun | n/a |  | Suggestion: "a person [who says false things(lies) about the things [that a person saw/witnessed]]" |  |  |
| false-witness | Phrase | n/a |  | Suggestion: "a person [who says false things(lies) about the things//events [that a person saw/witnessed]]" |  |  |
| favoritism | Noun | n/a |  | Suggestions: "treat some people well [while treating other people badly]" or "X treats the people [that X likes] well. But treats the people [that X does not like] badly" | show favoritism |  |
| filth | Noun | n/a |  | Use "dirt" for literal dirt. Possibly supply a dynamic alternate if it is representing something spiritual. |  |  |
| filthy-talk | Phrase | n/a |  | Suggestion: Use something like “words [that X should not say]” |  |  |
| first-fruits | Noun | n/a |  | Suggestion: something like "the first part of X [that people gathered-B//got//grew//harvested]" |  |  |
| flatter | Verb | n/a |  | Suggestion: "say words/things-C [that are not honest] about X [in order to please X]" | flatter X |  |
| flee | Verb | n/a |  | Use "run-away from" |  |  |
| flog | Verb | n/a |  | Use “whip” |  |  |
| folly | Noun | n/a |  | Suggestion: “stupid//foolish things-D//thoughts//things-B//things-C” |  |  |
| formerly | Adverb | n/a |  | Use "previously" |  |  |
| fowler | Noun | n/a |  | Suggestions: You could use something like "person [who hunts birds]" or in some contexts just use "person" |  |  |
| full (moon) | Adjective | n/a |  | Suggestion: Use “biggest” or “round”. |  |  |
| gaze | Noun | n/a |  | Suggestion: use "see" |  |  |
| gittith | Noun | n/a |  | Since this word is only used three times in the Bible and the meaning is not known, I suggest that we omit this |  |  |
| give-glory-to | Verb | n/a |  | Use "honored/glorified" or "praised/glorified" |  |  |
| gloat | Verb | n/a |  | Suggestion: something like “show [you are happy…” or “rejoice” |  | not for now |
| gospel | Noun | n/a |  | Use “Good-News” |  |  |
| gossip | Noun | n/a |  | Suggestion: Something like "talk about the things [that X does//says]" |  |  |
| gravel | Noun | n/a |  | Suggestion: “small stones and sand” |  |  |
| greed | Noun | n/a |  | Try to use greedy |  |  |
| grind | Verb | n/a |  | Suggestion: use “crush” or “rub” |  |  |
| grudgingly | Adverb | n/a |  | Suggestion: use "regret" |  |  |
| guarantee | Verb | n/a |  | Try to use “promise” instead |  |  |
| guardian-Redeemer | Noun | n/a |  | see “kinsman-redeemer” |  |  |
| guidance | Noun | n/a |  | Use “advice” |  |  |
| harass | Verb | n/a |  | Suggestion: something like "cause[ X to suffer]" |  |  |
| hardened | Adjective | n/a |  | Suggestion: Use something like "be not willing [to change]" |  |  |
| haughty | Adjective | n/a |  | Suggestions: use “proud-A” or “a person [who thinks [a person is better than other people]]” |  |  |
| hawk | Noun | n/a |  | Suggestion: something like "bird [that hunts smaller birds and small animals] " or "bird [that hunts animals] [and that has wide wings]" |  |  |
| heavy-heart | Noun | n/a |  | Try to use “very sad” | have a heavy-heart |  |
| heed | Verb | n/a |  | Use “listen” | give heed to |  |
| heir | Noun | n/a |  | Use “inherit” |  |  |
| Herodian | Noun | n/a |  | “people [who supported King _implicit Herod]” |  |  |
| heron | Noun | n/a |  | Suggestion: something like "bird [that has long legs] [and that eats fish]" or "water bird [that has long legs]" |  |  |
| hew | Verb | n/a |  | Use "chop" |  |  |
| high-fever | Noun | n/a |  | Suggestion: "very bad fever" |  |  |
| highway | Noun | n/a |  | Suggestion: use “wide road” |  |  |
| honeycomb | Noun | n/a |  | Suggestion: see if just “honey” would be adequate or include “insects/bees” somehow. I can’t think of a good explication and it’s only used 5 times |  | not for now |
| hoof | Noun | n/a |  | Suggestion: use "hard foot" |  |  |
| hoopoe | Noun | n/a |  | Suggestion: "small bird [that has tall feathers on small bird's head]" |  |  |
| house-of-X | Noun | n/a |  | Use "family" or "family/household". But use "family" when it means long term descendents |  |  |
| how | Adverb | n/a |  | Some options we have used include "extremely much" and "Null/behold!" | like in "How I love your law!" - not to be confused with the question word |  |
| humiliated | Adjective | n/a |  | Use “ashamed” |  |  |
| hunter | Noun | n/a |  | Generic: “person [who hunts animals]”. Also “man//woman [who hunts animals]” |  |  |
| hyrax-shafan-coney | Noun | n/a |  | describe it in the context of the passage like in Proverbs 30:26 |  |  |
| hyssop | Noun | n/a |  | Use "plant-hyssop" |  |  |
| idle | Adjective | n/a |  | Suggestion: use something like "does not work" |  |  |
| idolatry | Noun | n/a |  | Suggestion: something like “X serves/worship objects/idols [that X thinks [are gods]]” | do idolatry |  |
| ill | Adjective | n/a |  | Use “sick” |  |  |
| illegitimate | Adjective | n/a |  | Suggestion: something like “children [who were birthed by parents [who did not marry each-other(parents)]]” | illegitimate children |  |
| image | Noun | n/a |  | Use "statue" instead | image of X (meaning a statue of X) |  |
| immorality | Noun | n/a |  | Suggestion: "sexual bad-B actions = sexual sins" or just "bad-B actions = sins" |  |  |
| In-any-way | Phrase | n/a |  | Sometimes just delete it, or use “completely” or “always” |  |  |
| in-our-place | Phrase | n/a |  | Suggestion: use “Instead of” or “because of” or a beneficiary argument ("for") |  |  |
| in-the-same-way | Phrase | n/a |  | Use “similarly” |  |  |
| indignant | Adjective | n/a |  | Suggestion: "upset and angry" |  |  |
| inform | Verb | n/a |  | Use “tell” or “cause [X to know about Y]” | Inform X about Y |  |
| inheritance | Noun | n/a |  | use "inherit" |  |  |
| injured | Adjective | n/a |  | Use the noun or verb form |  |  |
| Inner-being | Phrase | n/a |  | Suggestion: use the person. For instance, to say “in your inner being”, use “inside you” |  |  |
| integrity | Noun | n/a |  | Suggestion: try to use "honest". |  |  |
| intentionally | Adverb | n/a |  | Suggestion: use “willingly” |  |  |
| intently | Adverb | n/a |  | Use “looked/stared hard”, which in English can be converted by a theta grid adjustment rule to "stared intently" (based on Tod’s comment to Mark 8:25) |  |  |
| interfere | Verb | n/a |  | Suggestion: Use “prevent [...” or “try [to prevent […]” |  |  |
| invisible | Adjective | n/a |  | “X [that people are not able [to see]]” | invisible X |  |
| invoke | Verb | n/a |  | Use “say” |  |  |
| jailer | Noun | n/a |  | Suggestion: “man//person [who is responsible for the prisoners]” or “...people [who are in the prison]]” |  |  |
| jasper | Noun | n/a |  | Suggestion: use something like "valuable/precious red stone". |  |  |
| Jesus-of-Nazareth | Noun | n/a |  | Use “Jesus [who is from Nazareth]” |  |  |
| Jesus’s-disciple | Noun | n/a |  | See "X's disciple" |  | suggest that we get rid of this |
| journey | Noun | n/a |  | Suggestion: Try to use the verb “travel” |  |  |
| judgment-day | Phrase | n/a |  | Use “the day [that God will judge all the people of the earth _optional on]” |  |  |
| juice | Noun | n/a |  | Suggestion: something like "drink [that is made from fruit by people _implicitActiveAgent]" |  |  |
| justified | Adjective | n/a |  | Suggestion: "God _implicitNecessary thinks/considers [X is good-B/blameless]" or "good-B/righteous" in Romans 3 | X is justified |  |
| kite | Noun | n/a |  | Suggestion: see wording for "hawk". A "kite" could be a small hawk |  |  |
| large | Adjective | n/a |  | Use “big” |  |  |
| Last-Days | Noun | n/a |  | Suggestion: "the last days [that are before the day//time (implicit-background) [that God will judge all the people of the world on//at]]" |  |  |
| lend | Verb | n/a |  | Use “loan” |  |  |
| likewise | Adverb | n/a |  | Use “similarly” |  |  |
| list | Verb | n/a |  | Use “list_noun” or some other wording |  |  |
| living | Adjective | n/a |  | Suggestion: something like “X that causes [people to live forever _optional]” | living X(noun like water?) |  |
| lizard | Noun | n/a |  | Suggestion: something like "small animal/reptile [that has four legs and a long tail]". |  |  |
| loathe | Verb | n/a |  | Usually use “hate”. see also "despise". |  |  |
| lose-heart | Verb | n/a |  | Suggestion: use "become sad/discouraged" |  |  |
| lover | Noun | n/a |  | Suggestion: something like "people [who love//sex each other]" or "a person [who loves//sexes X]" or "a person [who loves a person _2 [who loves a person]]". Also see "prostitute" |  |  |
| luxurious | Adjective | n/a |  | Try to use “comfortable” |  |  |
| luxury | Noun | n/a |  | Try to use “comfortable” |  |  |
| majestic | Adjective | n/a |  | Suggestion: use "great" or "glorious" |  |  |
| make-sure-that | Verb | n/a |  | Suggestions: “Be careful to”, “become sure that”, or some other construction |  |  |
| make-X(noun)-Y(adjective) | Verb | n/a |  | Suggestion: “cause [X to be Y]” | make X(noun) Y(adj) | no for now |
| malice | Noun | n/a |  | Suggestion: Use something like “do things [in order to harm other people]” |  |  |
| manure | Noun | n/a |  |  |  |  |
| marrow | Noun | n/a |  | Suggestion: "these soft inner part of bones" |  |  |
| marvelous | Adjective | n/a |  | Use “great/wonderful” |  |  |
| may | Verb | n/a |  | Use “Pray-hope [that …]” or use jussive “Let …” | may something happen | Not exactly |
| mean | Adjective | n/a |  | Suggestion: use “cruel” |  |  |
| Medes | Noun | n/a |  | Use "people of Media" |  |  |
| mediate | Verb | n/a |  | Suggestion: something like "causes X to have a relationship with Y" or you might use "through-B" |  |  |
| mediator | Noun | n/a |  | See "mediate" |  |  |
| melon | Noun | n/a |  | Suggestion: 'round fruit [that is (implicit-situational) big] [and that contains much-many water]' |  |  |
| miktam | Noun | n/a |  | Since the meaning of this word is not known and it's only used six times, I'm suggesting that we just use "poem". |  |  |
| millstone | Noun | n/a |  | Suggestion: "a stone [that people use for crushing grain]" |  |  |
| money-changer | Noun | n/a |  | “person [who sells/trades _routinely money]” |  |  |
| more-and-more | Adverb | n/a |  | You can do this now, or use “very many” or “much more” |  |  |
| motion | Verb | n/a |  | Suggestion: use something like "X moved X's hand [in order to show Y [...]]" | motion to someone |  |
| native-born | Adjective | n/a |  | use 'who was X [when he//she was born]' | X is native-born |  |
| needy | Adjective | n/a |  | Suggestion: "people [who need help]" |  |  |
| next-to | Phrase | n/a |  | Use "beside" |  |  |
| offer-that-(speech) | Verb | n/a |  | Suggestion: use “say” |  |  |
| oracle | Noun | n/a |  | Suggestion: Use something like "Yahweh//God//Lord//a god caused [X to write//say these words]" or "message/prophesy" |  |  |
| ordain | Verb | n/a |  | Suggestion: choose/appoint-B [X to be a priest] | ordain X |  |
| ordination-A | Noun | n/a |  | Suggestion: X is chosen/anointed <<by the LORD>> | ordination of X |  |
| osprey | Noun | n/a |  | Suggestion: "big bird [that hunts fish]" |  |  |
| paradise | Noun | n/a |  | Suggestion: "God's _implicit perfectly good place" |  |  |
| park | Noun | n/a |  | Suggestion: use something like "public place/land-B [that has trees and special plants]" |  |  |
| passion | Noun | n/a |  | Suggestion: use “feeling” |  |  |
| perceive | Verb | n/a |  | Suggestions: notice,know,understand,learn, realize |  |  |
| perjurer | Noun | n/a |  | Suggestion: "person [who says false things-C _speech to judges or rulers [after that person promised [to tell the truth]]]" |  |  |
| permission | Noun | n/a |  | Try to use "permit" |  |  |
| perplexed | Adjective | n/a |  |  |  |  |
| persevere | Verb | n/a |  | Suggestion: Use something like "X continues to do so-and-so [even though [X does so-and-so] is hard-B]" - the main idea is captured by the feature "continue to" |  |  |
| pillow | Noun | n/a |  | Suggestion: “bag [that has soft material inside that bag]” |  | we previously had "yes", but I don't see why we need it |
| pledge | Verb | n/a |  | Use "promise" |  |  |
| pound(Roman) | Noun | n/a |  | Use “about 0.3 kilograms” |  |  |
| presence | Noun | n/a |  | Suggestion:  Use "in front of" | in the presence of |  |
| prune | Verb | n/a |  | Suggestion: use "trim" |  |  |
| put-faith-in | Phrase | n/a |  | Use “believe in” |  |  |
| quick-tempered | Adjective | n/a |  | Suggestion: "becomes angry quickly" | be quick-tempered |  |
| rags | Noun | n/a |  | Suggestion: “old cloths”, maybe with “[that people use [in order to clean things]]” |  |  |
| raise-B | Verb | n/a |  | Use “X causes [Y to become alive again]” - in English this is generated as X raises Y from the dead through a transfer rule, but there is no word "raise" with this meeting in the ontology | raise from the dead |  |
| ransom | Noun | n/a |  | Suggestion: Try to use “money” with “free” |  |  |
| rashly | Adverb | n/a |  | See “reckless” |  |  |
| rather | Conjunction | n/a |  | Use "instead" |  |  |
| ravenous | Adjective | n/a |  | Use "very//extremely hungry" |  |  |
| rebuild | Verb | n/a |  | Suggestion: Use “build again” |  |  |
| reckless | Adjective | n/a |  | Suggestion: "a person [who does not think about the things [that a person says//does]]" | reckless person |  |
| refine | Verb | n/a |  | burn X [in order to cause [X to become pure-A]] | refine X |  |
| rely | Verb | n/a |  | Use “trust in” | rely on |  |
| rely | Verb | n/a |  | Use "depend" |  |  |
| remove | Verb | n/a |  | Use “take-away” |  |  |
| repeat | Verb | n/a |  | Use “say//do again” |  | not for now |
| reputation | Noun | n/a |  | Suggestion: rewrite using “respect_verb” |  |  |
| reputation | Noun | n/a |  | Suggestion: use “People respect X” | To have a good reputation |  |
| request | Noun | n/a |  | Suggestion: “thing-B [that X asked for]” | X's request |  |
| respond | Verb | n/a |  | Use "reply" |  |  |
| restitution | Noun | n/a |  | Suggestion: "X pays Y to Z [because X...]" or perhaps "X pays Y to Z because of X's actions" where the "because" clause or noun phrase explains the reason for the payment. |  |  |
| revelation | Noun | n/a |  | Suggestion: “ messages of God” or “ messages [that come from God]” | revelation (messages from God) |  |
| revile | Verb | n/a |  | Suggestion: “X shows [that X does not respect Y] [by insulting Y]”. Or consider “insult”. See also “scorn”. |  |  |
| rightly | Adverb | n/a |  | Suggestion: use “well” |  |  |
| rise-from-the-dead | Verbal phrase | n/a |  | Use "become alive again" - in English, this may be generated as "rise from the dead" through a transfer rule, but there is no word "rise" with this meaning in the ontology |  |  |
| ritually | Adverb | n/a |  | use "religiously" |  |  |
| robber | Noun | n/a |  | Use “thief” |  |  |
| rock | Noun | n/a |  | Use “stone” | a rock |  |
| rot | Verb | n/a |  | Use “decay” |  |  |
| rub-out | Verb | n/a |  | Suggestion: use "blot-out" |  |  |
| ruby | Noun | n/a |  | In Proverbs 20:15, , used “jewel [that costs much money]” or "valuable/precious red stone". See TNN for suggestions. |  |  |
| ruthless | Adjective | n/a |  | Use “cruel” |  |  |
| sap-resin-bdellium | Noun | n/a |  | Suggestion: sticky liquid [that comes from a tree] |  |  |
| sapphire | Noun | n/a |  | Suggestion: “blue jewel” |  |  |
| scoff | Verb | n/a |  | Use “laugh/mock at” |  |  |
| scoundrel | Noun | n/a |  | Suggestion: “person [who is not valuable] -> worthless person” or “bad-B person” |  |  |
| seabird | Noun | n/a |  | Use "bird of sea" |  |  |
| self-control | Noun | n/a |  | Suggestion: Use a construction with “X controls X” |  |  |
| shackle | Noun | n/a |  | Use "chain" |  |  |
| shed | Verb | n/a |  | Suggestion: use "pour-out/spill" |  |  |
| shun | Verb | n/a |  | Suggestion: use “avoid” |  |  |
| simple | Adjective | n/a |  | Suggestion: "people [who do not know many things]" | referring to people |  |
| slap | Verb | n/a |  | Suggestion: “hit-A Y with X’s hand” | X slap Y |  |
| slay | Verb | n/a |  | Suggestion: use "kill" or "kill/slaughter" |  |  |
| sluggard | Noun | n/a |  | Use “lazy person” |  |  |
| sly | Adjective | n/a |  | Use "crafty" |  |  |
| something | Noun | n/a |  | Use “a thing” |  |  |
| sorcery | Noun | n/a |  | Suggestions: Use just “magic” or “magic of evil spirits” or “ magic [that uses the power of evil spirits]” |  |  |
| sorrow | Noun | n/a |  | Use “very sad” |  |  |
| sorrowful | Adjective | n/a |  | Use “very sad” |  |  |
| sovereign | Adjective | n/a |  | See NASB, that often uses "Lord-A". |  |  |
| speak-in-tongues | Verb | n/a |  | Suggestion: “X speaks in a language [that X does not understand]” |  |  |
| spent-body | Phrase | n/a |  | Suggestion: use “body is weak” |  |  |
| spine | Noun | n/a |  | Suggestion: Use "bone of back" |  |  |
| splendid | Adjective | n/a |  | Suggestion: beautiful//great//big |  | previously had yes, but I don't think we need this |
| stay-away-from | Verb | n/a |  | Use “avoid” |  |  |
| stillborn | Adjective | n/a |  | a child [who is dead [when a child is born]] | stillborn child |  |
| stir-up | Verb | level 2 |  | Suggestion: "cause X to become angry//upset" |  |  |
| stop | Verb | n/a |  | Suggestion: "Cause [X to stop doing Y]" | stop X from doing Y |  |
| storehouse | Noun | n/a |  | “room//building [that X stores things in]” |  |  |
| stork | Noun | n/a |  | Suggestion: "white bird [that eats fish] with long legs" |  |  |
| strife | Noun | n/a |  | Suggestion: use something like "People oppose each other" |  |  |
| stringed | Adjective | n/a |  | Use “that have strings” | stringed (instruments) |  |
| strip-off | Verb | n/a | take-off |  |  | previously had yes, but I don't think we need this |
| such | Adjective | n/a |  | Suggestion: "X _generic who are like those X” |  | previously had yes, but I don't think we need this |
| superior | Adjective | n/a |  | Use "better" - the comparative form of "good" |  |  |
| surely | Adverb | n/a |  | Use “certainly” (which will become a feature) |  |  |
| take-refuge | Verb | n/a |  | Use something like "I go to you in order to be safe". |  |  |
| tanner | Noun | n/a |  | Suggestion: “person [who makes things with leather]” |  |  |
| tassel | Noun | n/a |  | Suggestion: "a group of threads//cords//strings [that are joined at one end]" |  |  |
| taunt | Verb | n/a |  | Suggestion: use "insult" or "mock" |  |  |
| temper | Noun | n/a |  | Suggestion: use “becomes much//quickly angry” | has a temper or is hot//quick tempered |  |
| tempted | Adjective | n/a |  | “X want [to do bad-B things]” (For being tempted to do something on one’s own volition.) | X be tempted (by X) |  |
| the-heavens | Noun | n/a |  | This is "sky-B" |  |  |
| the-Last-Day | Noun | n/a |  | Suggestion: Use as a literal version with “last day” and include a dynamic version with “the day [that God will judge all of the people of the earth on]]” - see Cliq discussion - Or  "the last day [ _descriptive which God will judge (implicit-background) all the people of the world on]" |  |  |
| the_Lord’s-B_supper | Noun | n/a |  | Use “the Lord’s-B meal” |  |  |
| there-was-a-time-when | Phrase | n/a |  | Use “previously” |  |  |
| thrive | Verb | n/a |  | Use (complex) “flourish” |  |  |
| tilt | Verb | n/a | point |  |  |  |
| timbrel | Noun | n/a |  | Use "tambourine" |  |  |
| together | Adverb | n/a |  | Suggestion: you can just omit it, or in some circumstances you could say "with each-other(X)" |  |  |
| tolerate | Verb | n/a |  | Try using “accept” |  |  |
| too | Adverb | n/a |  | Use "also" |  |  |
| topic | Noun | n/a |  |  |  | not for now |
| tradesman | Noun | n/a |  | Suggestion: "person [who have skills]" |  |  |
| treasure | Verb | n/a |  | See “cherish” | treasure X |  |
| tribulation | Noun | n/a |  | Suggestion: use "time of much trouble". |  |  |
| true-disciple | Phrase | n/a |  | Suggestion: “person [who truly follows _routinely person]”; NOTE: You must ask P2 to block the rule for “X’s disciple” |  |  |
| true-prophet | Noun | n/a |  | "person [who tells true messages [that come from God] to people _generic]" | true prophet |  |
| trustworthy | Adjective | n/a |  | Use "faithful" or we write it using the verb "trust", like "person [that people trust]" |  |  |
| tsetUndefined | Noun | n/a |  | This is just to test what happens to an undefined word |  |  |
| turmoil | Noun | n/a |  | Suggestion: use “trouble” |  |  |
| twilight | Noun | n/a |  | Suggestion: “the time [that is during the evening] [and when the sky is becoming less bright]” |  | previously, I said yes, but I don't think we need it |
| unbeliever | Noun | n/a |  | suggestion:  something like "person [who does not believe in Jesus//Christ//God//Yahweh]" |  |  |
| unclean | Adjective | n/a |  | See “dirty-B” (= “unclean” in English). It's not a word in the semantic representation, but will be the English expression of “dirty-B” | unclean (religiously) | kind of |
| understanding | Noun | n/a |  | Use the verb “understand” |  |  |
| union | Noun | n/a |  | Suggestion: use the verb “unite” |  |  |
| unwilling | Adjective | n/a |  | Suggestion: use “not be willing” | be unwilling |  |
| value | Verb | n/a |  | Suggestion: “Think//know [that X is valuable]” | value X |  |
| vanish | Verb | n/a |  | Suggestion: Use something like “people suddenly stopped seeing X” |  |  |
| vat | Noun | n/a |  | “big container [that people store wine//oil in]” |  |  |
| verdict | Noun | n/a |  | Use "decision" or something like "things that X decided" |  |  |
| version | Noun | n/a | book | (pairing used for the concept of different versions of the Bible, NOT the same as copy/manuscript, which is used in footnotes about textual criticism issues) |  |  |
| victorious | Adjective | n/a |  | try to use "win" or "defeat" |  |  |
| victory | Noun | n/a |  | it’s in the LDV, but let’s see if we can use “win” or "defeat" |  | not for now |
| visible | Adjective | n/a |  | “X [that people are able [to see]]” | visible X |  |
| voluntarily | Adverb | n/a |  | Suggestion: use “willingly” - see at right. Previously suggested that we pair with “willingly” |  | I had yes previously, but I don’t think we need it. You can use "willing to" |
| warden | Noun | n/a |  | Suggestion: “man//person [who is responsible for the prisoners]” or “...people [who are in the prison]]” | prison warden |  |
| watch | Noun | n/a |  | Suggestion: "first part of the night", "middle of the night" or "middle part of the night", and "last part of the night" | Meaning a time period during the night |  |
| watchtower | Noun | n/a |  | “tower [where people _generic are able [to watch the garden//vineyard//city]]” |  |  |
| wealthy | Adjective | n/a |  | Suggestion: Use "rich" or "had much wealth" |  |  |
| wipe-away | Verb | n/a |  | Suggestion: use "blot-out" |  |  |
| woe | Noun | n/a | the | Suggestion: “<There will be> terrible trouble//events!” |  |  |
| woe | Noun | n/a |  | Suggestion: “X will suffer much” or “Terrible things will happen _implicitNecessary to X” | woe to X |  |
| yogurt | Noun | n/a |  | Suggestion: “a thick sour substance” (Prov 30:33) |  |  |

## Uncategorized (status not recorded in the source sheet)

1 entry where the source sheet left Status blank — verify live before use.

| Term | POS | Level | Paired with | Explication | Structure | Notes |
|---|---|---|---|---|---|---|
| plaster | Verb |  |  | Suggestion: use the noun form with something like "put plaster on..." or "cover ... with plaster" |  |  |

## List of exclamations

From the sheet's "list of exclamations" tab — interjections attested in Jeremiah, with the verses where each occurs. Included for reference; these are discourse particles rather than pairing/explication candidates, so cross-check `/simplification_hints` before encoding one.

| Exclamation | Attested at |
|---|---|
| O | Jer 3:14, 1:6, 1:11?, 2:4, 2:12, 2:31, 3:4?, 3:12? |
| Ah | Jer (Jeremiah, unspecified verse) |
| Alas | Jer 1:6, 4:10, 4:31, 6:4 |
| Oh! | Jer 4:19, 9:1, 9:2 |
| lo? | Jer 4:23, 4:24, 4:25, 4:26, 8:9 |

## Known-complex words with no how-to entry yet

From the sheet's "Other Complex Words in TBTA" tab — 71 words flagged as complex in the TBTA ontology but not yet covered by this how-to (no pairing, explication, or confirmed ontology entry recorded). Treat every one of these as level 2/3 by default — **do not use bare** — and look it up live via `/search` and `/simplification_hints` before encoding it; a live lookup may since have added an entry for one of these.

| Term | POS |
|---|---|
| cheese-A | Noun |
| embalm-A | Verb |
| enchanter-A | Noun |
| extraordinary-A | Adjective |
| fare-A | Noun |
| flake-A | Noun |
| friendly-A | Adjective |
| garbage-A | Noun |
| ghost-A | Noun |
| give-attention-A | Verb |
| gloriously-A | Adverb |
| glove-A | Noun |
| goad-A | Noun |
| grasp-A | Verb |
| hamstring-A | Verb |
| handsome-A | Adjective |
| hat-A | Noun |
| herald-A | Noun |
| hip-A | Noun |
| hornet-A | Noun |
| hover-A | Verb |
| inspect-A | Verb |
| ladder-A | Noun |
| lentil-A | Noun |
| limp-A | Verb |
| liver-A | Noun |
| make-up-A | Verb |
| mandrake-A | Noun |
| meditate-A | Verb |
| merchandise-A | Noun |
| midwife-A | Noun |
| mortar-A | Noun |
| nephew-A | Noun |
| nest-A | Noun |
| pastor-A | Noun |
| pick-A | Noun |
| pitchfork-A | Noun |
| princess-A | Noun |
| prudent-A | Adjective |
| quality-A | Noun |
| raid-A | Verb |
| recede-A | Verb |
| retreat-A | Verb |
| rib-A | Noun |
| scold-A | Verb |
| seek-attention-A | Verb |
| seizure-A | Noun |
| sign-A | Noun |
| sign-A | Verb |
| son-in-law-A | Noun |
| spill-A | Verb |
| stair-A | Noun |
| stalk-A | Noun |
| stranger-A | Noun |
| stripe-A | Noun |
| surrender-A | Verb |
| sweat-A | Verb |
| tar-A | Noun |
| teaspoon-A | Noun |
| towel-A | Noun |
| transform-A | Verb |
| treaty-A | Noun |
| trench-A | Noun |
| trip-A | Verb |
| trough-A | Noun |
| vaccine-A | Noun |
| vault-A | Noun |
| veil-A | Noun |
| violently-A | Adverb |
| wound-A | Verb |
| wrestle-A | Verb |
