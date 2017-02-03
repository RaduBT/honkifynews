#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import json
import re

base = {
    'schema': 'InsultMarkupLanguage/0.2',
    'refresh_age': 604800000,
    'run_info': {
        'count': 30,
        'startTimeout': 1000,
        'maxTimeout': 30000,
        'timeMultiplier': 1.8,
    },
    'whitelist': [
        "www.foxnews.com", "cnn.com", "www.bbc.com/news",
        "www.bbc.co.uk/news", "www.theguardian.com", "www.theguardian.co.uk",
        "nytimes.com", "facebook.com", "washingtonpost.com", "salon.com",
        "slate.com", "buzzfeed.com", "vox.com", "huffingtonpost.com",
        "wsj.com", "economist.com", "latimes.com", "dallasnews.com",
        "usatoday.com", "denverpost.com", "insidedenver.com", "philly.com",
        "chron.com", "detroitnews.com", "freep.com", "boston.com",
        "newsday.com", "startribune.com", "nypost.com", "ajc.com", "nj.com",
        "sfgate.com", "sfchronicle.com", "azcentral.com", "chicagotribune.com",
        "cleveland.com", "oregonlive.com", "tampatribune.com",
        "signonsandiego.com", "mercurynews.com", "contracostatimes.com",
        "insidebayarea.com", "feedly.com", "reddit.com",
        "drudgereport.com", "theblaze.com", "breitbart.com","ijreview.com",
        "newsmax.com", "wnd.com", "dailycaller.com", "washingtontimes.com",
        "nationalreview.com", "townhall.com", "freerepublic.com",
        "pjmedia.com", "hotair.com", "cnsnews.com", "westernjournalism.com",
        "washingtonexaminer.com", "tpnn.com", "newsbusters.org",
        "twitchy.com", "news.google.com", "npr.org",
    ],
    'actions': {
        'trump': {
            'find_regex': [
                "((Donald|DONALD)\\s*(J\\.?\\s*)?)?(Trump|TRUMP)(?!\\w)", "g"
            ],
            "img_find_regex": [
                "(\\b|_|[0-9])[Tt][Rr][Uu][Mm][Pp](\\b|_|[A-Z]|[0-9])",
                "g"
            ],
            'image_replacement': {
                'html': [
                    'National Disgrace Removed',
                    'Disturbing Imagery Blocked',
                    'You don\'t want to see what was here.',
                    'Detrumpified',
                ],
                'border': 1,
                'background': [
                    'http://www.toolsofourtools.org/detrumpify2/v2/houndstooth.png',
                    'http://www.toolsofourtools.org/detrumpify2/v2/floral.png',
                    'http://www.toolsofourtools.org/detrumpify2/v2/rope.png',
                ]
            },
            'randomize_mode': 'always',
        },
        'pence': {
            'find_regex': [
                "\\b((Mike|Michael)\\s*)?Pence(?!\\w)", "g"
            ],
            'randomize_mode': 'always',
        },
        'alt-right': {
            'find_regex': [
                "\\b(?!([Aa]|[Aa]n|[Tt]he)\\s)[Aa]lt[- ][Rr]ight(?!\\w)", "g",
            ],
            'randomize_mode': 'always',
        },
        'bannon': {
            'find_regex': [
                # first name and/or middle initial may be present
                # "((Steve|Steven|Stephen|STEVE|STEVEN|STEPHEN)\\s*((K\\.?|Kevin|KEVIN)\\s*)?)?(Bannon|BANNON)(?!\\w)", "g"
                # first name and/or middle initial must be present
                "((Steve|Steven|Stephen|STEVE|STEVEN|STEPHEN)\\s*((K\\.?|Kevin|KEVIN)\\s*)?)(Bannon|BANNON)(?!\\w)", "g"
            ],
            'randomize_mode': 'always',
        },
        'conway': {
            'find_regex': [
                "((KELLYANNE|Kellyanne)\\s*)?(Conway|CONWAY)(?!\\w)", "g"
            ],
            'randomize_mode': 'always',
        },
        'spicer': {
            'find_regex': [
                "((SEAN|Sean)\\s*)?(SPICER|Spicer)(?!\\w)", "g"
            ],
            'randomize_mode': 'always',
        },

    }
}

monikers = {
  'trump': {
    'clean': [
      "Gaffe-Prone Lunatic",
      "Human-Toupee Hybrid",
      "Decomposing Jack-O-Lantern",
      "Angry Creamsicle",
      "The Kindest, Bravest, Warmest, Most Wonderful Human Being You'll Ever Know in Your Life",
      "Walking Faux Luxury Brand",
      "Real-Estate Tycoon with Simple, Stupid Plan to Defeat ISIS",
      "Self-Proclaimed Ponderer of Incest",
      "Wall Construction Expert",
      "Frequent Provider of Unsolicited Judgements Regarding Female Attractiveness",
      "Unrepentant Birther",
      "Serial Propogator of Demonstrable Falsehoods",
      "Harkener to Unspecified Moment of American Greatness",
      "Master of Zero-Sum Business Deals",
      "Purveyor of Lousy Steak",
      "Angrily Reanimated Christmas Ham",
      "Short-Fingered Vulgarian",
      "Weirdly Authoritarian Gingerbread Man",
      "Traditional Values Adulterer with Two Ex-Wives",
      "Rage Tribble",
      "Unconvincing Presidential Simulation",
      "Scab You Wish You Hadn't Picked",
      "Idiot Media Savant",
      "Fiberglass-Topped Tantrum Thrower",
      "Used Q-tip",
      "Idiot Magnet",
      "Gender-Threatened Lead Paint Factory Explosion",
      "70's-Vintage Umber Shag Carpet",
      "Cheeto Jesus",
      "Bone-in Ham",
      "Four-Time Bankruptcy Filer and Seething Hernia Mass",
      "Sun-Dried Tomato",
      "Adult Blobfish",
      "Deflated Football",
      "Fart-Infused Lump of Raw Meat",
      "Melting Pig Carcass",
      "Disgraced Racist",
      "Talking Comb-Over",
      "Human Equivalent of Cargo Pants that Zip Away into Shorts",
      "Cheeto-Dusted Bloviator",
      "Fuzzy Meat-Wad",
      "Bag of Flour",
      "Man Who Cherishes Women",
      "Future Leader of the Free World",
      "Decomposing Ear of Corn",
      "Own Best Parody",
      "Rich Idiot Willing to Allow Garbage to Fall Out of His Mouth Without Batting a Single Golden Lash",
      "Pond Scum",
      "Noted Troll",
      "Class Clown that Everyone Wishes Would Be Quiet and Let The Class Learn",
      "Melting Businessman",
      "Wax Museum Figure on a Very Hot Day",
      "Soggy Burlap Sack",
      "Bag of Toxic Sludge",
      "President and Ruler for Life",
      "Brightly Burning Trash Fire",
      "Great Judgement-Haver",
      "Man-Sized Sebaceous Cyst",
      "Enlarged Pee-Splattered Sno Cone",
      "Empty Popcorn Bag Rotting in the Sun",
      "Man-Shaped Asbestos Insulation Board",
      "Hair Plug Swollen with Rancid Egg Whites",
      "Inside-Out Lower Intestine",
      "Dusty Barrel of Fermented Peepee",
      "Usually Reasonable Burlap Sack Full of Rancid Peeps",
      "Presidential Candidate and Bargain Bin Full of Yellowing Jean-Claude Van Damme Movies",
      "Hairpiece Come to Life",
      "Normal-Looking Human Man and Entirely Credible Choice as Future Leader of the Free World",
      "Decomposing Pumpkin Pie Inhabited by Vicious Albino Squirrels",
      "Dishrag that on Closer Inspection is Alive with Maggots",
      "Lead Paint Factory Explosion",
      "Candied Yam Riddled with Moldy Spider Carcasses",
      "Enraged Gak Spill",
      "Shriveled Pinto Bean You Had to Pluck out of Your Chipotle Burrito Basket",
      "Human-Sized Infectious Microbe",
      "Poorly-Trained Circus Organgutan",
      "Chester Cheetah Impersonator",
      "Lumbering Human-Size Tardigrade",
      "Tiny Piece of Dried Cat Poop that You Found in Your Rug",
      "Seagull Dipped in Tikka Masala",
      "Bursting Landfill of Municipal Solid Waste",
      "Mountain of Rotting Whale Blubber",
      "Sputum-Filled Orange Julius",
      "Orange Julius Caesar",
      "Gangrenous Gaping Wound",
      "Racist, Sexist Block of Aged Cheddar",
      "Oversized Wasp Exoskeleton Stuffed with Old Mustard",
      "Neo-Fascist Real Estate Golem",
      "Abandoned Roadside Ham Hock",
      "Bewildered, Golden-Helmeted Astronaut Who’s Just Landed on This Planet from a Distant Galaxy",
      "Monument to Human Hubris Crafted out of Rotting Spam",
      "Walking Pile of Reanimated Roadkill",
      "Heaving Carcass",
      "Stately Hot Dog Casing",
      "Flatulent Leather Couch",
      "Swollen Earthworm Gizzard",
      "Narcissistic Bowl of Rotten Gazpacho",
      "Yellowing Hunk of Masticated Gristle",
      "Human/Komodo Dragon Hybrid",
      "Blackening Scab Artfully Hiding in Your Raisin Bran",
      "“Taco truck”",
      "Man Who Could One Day Become the First Hobgoblin to Enter The White House",
      "Pair of Chapped Lips Superglued to a Hairball",
      "Horsehair Mattress Stuffed with Molding Copies of Hustler",
      "Malignant Corn Chip",
      "Human Kinder Egg Whose Inner Surprise is a Tiny Pebble of Rat Shit",
      "The Sculpture your Three-Year-Old Made out of Soggy Ground-Up Goldfish Snacks",
      "Man with the Hair of a Radioactive Skunk",
      "Roiling Cheez Whiz Mass",
      "Cryogenically Frozen Bog Man",
      "Glistening, Shouting Gristle Mass with a History of Saying Terrible and Stupid Things",
      "Screaming Giant Cheese Wedge",
      "250-pound Accumulation of Rancid Beef",
      "Day-Glo Roadside Billboard About Jock Itch",
      "Temperamental Gelatinous Sponge",
      "Sentient Hate-Balloon",
      "Rumpelstiltskin Inflated with a Bike Pump and Filled with Bacteria",
      "Self-Tanning Enthusiast",
      "Enraged, Bewigged Fetus Blown up to Nightmarish Size",
      "Parental Pile of Burnt Organic Material",
      "Human-Shaped Wad of Gak",
      "Walking Irradiated Tumor",
      "Uncooked Chicken Breast",
      "KKK Rally Port-a-Potty Holding Tank",
      "Neon-Tinted Hellion",
      "Plentiful Field of Dung Piled into the Shape of a President",
      "Malfunctioning Wind Turbine",
      "Seeping Fleabag",
      "Sloshing Styrofoam Takeout Container Filled with Three-Day-Old Mac and Cheese",
      "Sticky, Grabby, Cheeto-Hued Toddler with No Sense of Adult Deportment",
      "Figurative Rubber, and also Literal Rubber",
      "Carnivorous Plant Watered with Irradiated Bat Urine",
      "Sentient Waste Disposal Plant",
      "Disappointment",
      "Poorly-Drawn Fascist",
      "Racist Teratoma",
      "Lamprey Eel Spray-Painted Gold",
      "Hair That You Pluck, Causing a Cluster of Hairs to Sprout in Its Place",
      "Sunken, Corroding Soufflé",
      "Nacho Cheese Golem",
      "Undead Tangerine",
      "Cartoon Representation of Irritable Bowel Syndrome in a Pharmaceutical Ad",
      "Fossilized Meatball",
      "Horking Mole-Creature Suffering from Radioactive Spray-Tan",
      "Tattered Craigslist Sofa",
      "Full-Grown Monopoly Dog Carefully Balancing a Spongecake Atop His Head",
      "Play-Doh Factory Explosion",
      "New Superfood Made of Finely-Ground Clown Wigs",
      "Unkempt Troll Doll Found Floating Facedown in a Tub of Rancid Beluga Caviar",
      "Cheeto-Faced Ferret",
      "Orange Muppet",
      "Mangled Apricot Hellbeast",
      "Little Gloves",
      "Numpty",
      "Weapons-Grade Plum",
      "Hair Fuehrer",
      "Man-Baby",
      "Ambitious Corn Dog that Escaped from the Concession Stand at a Rural Alabama Fairground, Stole an Unattended Wig, Hopped a Freight Train to Atlantic City and Never Looked Back",
      "Ugly Racist",
      "Wealthy Inheritor Disguised as Successful Businessman",
      "National Embarrassment",
      "Wart We Can't Freeze Off Until November 2020",
      "Microwaved Circus Peanut",
      "Talking Dingleberry",
      "Republican Babadook",
      "El Caudillo de Mar-a-Lago",
      "Shouting, Rotting Papaya",
      "Impotent Orangutan",
      "Famed Shouting Tycoon",
      "Mutant Carrot",
      "Spittle-Flecked Carrot",
      "Epic Fart that Just Won't Dissipate",
      "Gibberish Volcano",
      "Shaved Tribble",
      "Pile of Rotten Orange Peels in a Suit",
      "Rotting Pumpkin",
      "Deplorables Coach",
      "Putin Puppet",
      "Projector-in-Chief",
      "Soon-to-be-Fired Reality Show Contestant",
      "Unreliable Narrator of Awful Story",
      "Biff Tannen",
      "Swirling Black Hole that Eats Good Sense",
      "Self-Avowed Perpetrator of Sexual Assault",
      "President Worse Than W, Despite How Improbable That Used to Sound",
      "Sociopathic Operating System Installed on a Frightened Child",
      "Everything Wrong with America, Made into Living Flesh",
      "Manchurian Combover",
      "Cheeto Benito",
      "Scammer-in-Chief",
      "Gigantic Rubbery Manchild",
      "Pompous Suit Balloon",
      "Two-bit Monorail Salesman",
      "Self-Absorbed Git",
      "Gilded Walking Viagra Advertisement",
      "Professional Fraudster",
      "Toupee-Wearing Ball of Spite",
      "Uncooked Bread Dough",
      "Stubby-Fingered Coatfart",
      "World's Most Easily Insulted Fascist Buffoon",
      "Triple-Chinned Bull in a Nuclear China Shop",
      "Trumplethinskin",
      "Twitter Twit",
      "Human Traffic Cone",
      "Dog that Caught the Car",
      "Thin-Skinned Idiot with Nuclear Codes",
      "Grifter-in-Chief",
      "Sentient Caps-Lock Button",
      "Xenophobic Sweet Potato",
      "Batman Villain",
      "Rome Burning, in Man Form",
      "Buffalo Wing that Fell in a Urinal",
      "America's Back Mole",
      "Rain Man of Manipulative Bullshit",
      "World's Largest Troll Doll",
      "Melting Orange Popsicle",
      "Dessicated, Hollowed-Out Pumpkin Stuff With Wasps",
      "Rusted Refrigerator Left in The Sun Until Its Contents Rot And Swell Into A Noxious, Congealed Mass",
      "Regurgitated Wombat",
      "Moldy Pumpkin Spite Latte",
      "Tax-Avoidant Opossum Testicle",
      "Shrieking Carbuncle in a Red Power Tie",
      "Chipotle Burrito Taken to Its Natural, Digested Conclusion",
      "Evil Toddle",
      "Clump of Moldering Drain Hair",
      "Inlfated Pig Stomach Full of Rotten Pierogi",
      "Flatulent Butternut Squash",
      "Putrescent Orange Marshmallow",
      "Pilonidal Cyst",
      "Sexist Sentient Carrot",
      "Abandoned Cruise Ship Full of People Afflicted with Norovirus",
      "Bruised Yam",
      "Overflowing Litter Box",
      "Shaved Bear",
      "Demonic, Racist Goldfish",
      "Long and Thunderous Fart in a Stalled Elevator",
      "Rancid Halloween Oreo Filling",
      "Rage-Addled Oompa Loompa",
      "Bewigged Swollen Gall Bladder",
      "Wheezing Blurg from Endor's Forest Moon",
      "Inflamed Carbuncle",
      "Diet of Templeton The Rat",
      "Soggy Cracker Spread with Spoiled Shrimp Compote",
      "Industrial-Sized Wastebasket in a Clip-On Tie",
      "Impacted Molar",
      "Bag of Hot Garbage Moldering in the Summer Sun",
      "Dry Creek Bed Mysteriously Studded with Dog Turds",
      "Haunted Bidet",
      "Yellowing Mop Dripping with an Unidentifiable, Viscous Fluid",
      "Anthropomorphic Lie",
      "Rooster Who Wandered Into the House and Has to be Restrained Beneath a Metal Wastebasket",
      "Political Equivalent of One of Those Mutant Factory Farm Chickens with Breasts So Big It Can't Walk",
      "Spray-Tanned Blobfish",
      "Parking Cone with Emotional Issues",
      "Moldy Prawn Burrito",
      "Gelatinous Heap",
      "Horrible Man with Hair Like Used Dental Floss and Ideas That Thread The Definition of Democracy",
      "Hexed Tub of Velveeta That's Been Brought to Life and Won't Stop Screaming Racist Insults",
      "Scabies Outbreak in Your Freshman Dorm",
      "Fetid Pooh-Face",
      "Floopy Sack of Rancid Chicken Fat",
      "Cicade Husk Dipped in Fermenting Carrot Soup",
      "Cirrhotic Cheetah Liver Dusted in Gold Leaf",
      "Walking Staph Infection",
      "Large Orange Baby",
      "Besuited Chucky Doll",
      "Objectively Horrible Person",
      "Toxic Algae Bloom",
      "Spicy Asbestos-Flavored Dorito",
      "Snot-Flavored Jelly Bean with Frightening Power and Influence",
      "Decaying, Hollowed-Out Tree Trunk That Houses a Family of Malnourished Possums",
      "Enlarged Brick of Spittle-Flecked Crisco",
      "Gold-Tipped Mucous Plug",
      "Melted Claymation Villain",
      "Unwashed Fumigation Tent",
      "One of Those Piles of Sand by The Highway",
      "Moldering Cheez-It",
      "Hunk of Beef Jerky That Rolls Under The Couch And Is Left to Harden, Becoming Covered in Dust and Cat Hair Until a Cockroach Takes it Back to Its Lair and Makes It His Wife",
      "Three Bigoted Baby Muppets Stacked On Top of Each Other",
      "Half-Melted Pile of Candy Corn from Halloween '83",
      "Giant Mound of Hardened Cheez Whiz",
      "Smushed up Caterpillar Your 6-Year-Old Brother Set On Fire With a Magnifying Glass",
      "Rotten Kabocha Squash",
      "Orange Roughy",
      "Saglutupiaġataq",
      "National Grand Mal Seizure",
      "Champion of Oppressors",
      "Angry Postule",
      "Dolt 45",
      "Combover Caligula",
      "Mango Manchurian",
      "Idiot Amin",
      "Twitler",
      "Der Gropenführer",
      "Cheez Whiz Ceaușescu",
      "Passionfruit Pinochet",
      "Darth Hater",
      "Lord Goldemort",
      "Littlefingers",
      "Mango Chucky",
      "Tangerine Torquemada",
      "Sociopathic Potato",
      "Boss Tweet",
      "Marmalade Mussolini",
      "Furious Orange",
      "Cheetle Golem",
      "Jack the Twitter",
      "Lyssavirus Agglutination",
      "Tribble Mobility Scooter",
      "Con Fartiste",
      "Pinochetio",
      "Tribble Threat",
      "Saffron Suharto",
      "Manchurian Manchild",
      "Pyschopathic Elmer Fudd",
      "Orange Woundwort",
      "Dorito Mussolini",
      "Neon Nero",
      "Reliable Emetic",
      "Emperor Tangerine McTinyhands",
      "Narcissist-in-Chief",
      "Bannon's Burnt Orange Marionette",
    ],
    'dirty': [
      "Fuckface von Clownstick",
      "Billionaire and Person Who, Having Won the Fucking Presidency Without Any Qualifications, Inexplicably Believes the World is Set Against Him",
      "Political Ass Clown",
      "Vacuous Dipshit",
      "Degloved Zoo Penis",
      "Shithead",
      "Orange Asshat",
      "Idiot Cockwomble",
      "Ludicrous Tangerine Ballbag",
      "Incompressible Jizztrumpet",
      "Ferret-Wearing Shitgibbon",
      "Witless Fucking Cocksplat",
      "Buttplug Face",
      "Toupeed Fucktrumpet",
      "Human Turd",
      "High Oracle of Dipshittery",
      "Anus Lips",
      "Foul-Mouthed Tit Judge",
      "Baboon Anus",
      "Orange Condom Filled with Rancid Stew",
      "Used Diaphragm from the Jersey Shore",
      "Human Queef",
      "Noted Chode",
      "Man Whose Head Firmly Resembles a Lone Radioactive Testicle Sealed in a Jar of Formaldehyde",
      "Super Callous Fragile Racist Sexist Nazi POTUS",
      "Weeping Herpe Sore",
      "Donald Putinobitch",
      "Il Douche",
      "Goldman's Sack",
      "Dick l'Orange",
      "Badhair al-Asshead",
      "Garfrield's Scrotal Cancer",
      "Cockjerk Orange",
      "Blithering Butthole",
      "Scrooge McFuck",
      "America's #2",
      "Lord Dampnut",
      "Your Shitty Racist Uncle",
    ],
  },
  'alt-right': {
    'clean': [
      "Alt-Very-Wrong",
      "Serioualy-These-Are-Bad-People-Right",
      "Rebranded-White-Nationalist-Cult",
      "Hate-Filled-Right",
      "White-Supremacist-Movement",
      "Racist-Lunatic-Right",
      "Anti-Semitic-Monsters",
      "Misogynist-Cult",
      "Oft-Wrong",
      "Confederacy-of-Psychopathic-Dunces",
    ],
    'dirty': [
      "Fucking-Scary-Right",
    ],
  },
  'pence': {
    'clean': [
      "Dead-Ended Politician with Apparently Very Little to Lose",
      "Man Who Has Probably Tried To Outlaw Dancing",
      "Champion of Homophobic Pizza Makers",
      "Numbnuts Sidekick",
      "Total Failure as a Congressman",
      "Emcee Pink",
      "I'm with Stupid",
      "Focus of Chris Christie's Unrelenting Jealous Rage",
      "Mini-Bigot",
      "Supposedly Solid, Solid Person",
      "Rush Limbaugh on Decaf, Except Never Funny",
      "Six Term Congressman with Perfect Record of Writing Zero Bills that Became Law",
      "Angry Second-Assistant High School Football Coach",
      "Person Correct About Global Warming, Probably, in Some Distant Parallel Universe",
      "Man to Be Remembered Primarily for His Willingness to Be Associated with Donald Trump",
      "Conservative-Looking Guy Sent from Central Casting",
      "Presidential Apprentice",
    ],
    'dirty' : [
    ],
  },
  'bannon': {
    'clean' : [
      'Whiskey-Soaked Machiavelli',
      'Unshaven Emperor Palpatine',
      'Goebbels Acolyte'
      'Coke-Addled Dorito-Huffing Rasputin',
      'Fascist Puppeteer',
      'Plotter Against America',
      'Constitutional Demolitions Director',
      'White Nationalist Potato Sack',
      'Shiva, Destroyer of Rights',
      'Man Who, in a Just Universse, Would Warm a Barstool Alone Every Night Before Returning to His Empty Trailer',
      'Rumpled Suit With The President\'s Ear',
      'Leader of the Leader of the Free World',
      'Bigot Whisperer',
    ],
    'dirty': [
      'Neo Nazi Dickhead',
      'Repulsive, Plotting Shit',
    ]
  },
  'conway': {
    'clean' : [
      'Empty Shell That Might Once Have Been Occupied by a Human',
      'Alternative Fact Peddler',
      'Kellyanne Con-Artist',
      'Deputy Assistant Trump Boot Licker',
      'Suspected Trump Hostage',
      'Expert Liar',
      'Truth Mutilator',
      'Word Salad Dressing',
      'Robot Sent From The Future to Obliterate The Very Idea of Shared Reality',
      'Rhetorical IED',
    ],
    'dirty' : [
    ],
  },
  'spicer': {
    'clean': [
      'Mouth of Sauron',
      'Crack Hamster',
      'Inexpert Liar',
      'Man Who Permanently Destroyed All Credibility pn First Day of Job',
    ],
    'dirty': [
    ],
  },
}

url_base = 'http://toolsofourtools.org/detrumpify2/v2/'

combos = {
    'disable.json': {
        'monikers': [],
        'button': {
            'name': 'Disable Detrumpify',
            'description': 'Temporarily disable Detrumpify',
        },
    },
    'combined.json': {
        'monikers': ['clean', 'dirty'],
        'button': {
          'name': 'clean + NSFW insults',
          'description': 'Combined list of clean and dirty names.',
        },
    },
    'clean.json': {
        'monikers': ['clean', ],
        'button': {
          'name': 'clean insults',
          'description': 'Clean names only.',
        },
    },
    'dirty.json': {
        'monikers': ['dirty', ],
        'button': {
          'name': 'NSFW insults',
          'description': 'Only curseword names.'
        },
    },
}

for comboname in combos:

    outdata = copy.deepcopy(base)
    empty_actions = []
    for person in ['trump','pence','alt-right','bannon']:
    #for person in monikers:
      outdata['actions'][person]['monikers'] = []
      for moniker_group in combos[comboname]['monikers']:
        for moniker in monikers[person][moniker_group]:
          max_len = combos[comboname].get('max_len',0)
          if max_len:
              act_len = len(re.split(r'[\s\-]',moniker))
              if act_len <= max_len:
                  outdata['actions'][person]['monikers'].append(moniker)
          else:
              outdata['actions'][person]['monikers'].append(moniker)

      for v in ['randomize_mode', 'match_style', 'match_class', 'bracket']:
        if v in combos[comboname]:
          outdata['actions'][person][v] = combos[comboname][v]

      if len(outdata['actions'][person]['monikers']) < 1:
        empty_actions.append(person)

    for action in empty_actions:
      outdata['actions'].pop(action,None)

    jsd = json.dumps(outdata)
    ofile = open(comboname, 'w')
    ofile.write(jsd)
    ofile.close()

ofile = open("insults.txt", "wb")
for moniker in sorted(monikers['trump']['clean']):
    ofile.write('"' + moniker + '",' + "\n")
ofile.close()


## button config file
bconfig = []
for comboname in combos:
  combos[comboname]['button']['url'] = url_base + comboname
  bconfig.append(combos[comboname]['button'])

bconfig.append({
  'name': 'Drumpf',
  'url': url_base + 'drumpf.json',
  'description': 'Always Drumpf (John Oliver mode)'
});

ofile = open('buttons_config.json',"w")
ofile.write(json.dumps(bconfig))
ofile.close()
