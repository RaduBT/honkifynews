var replacements = [
"70's-Vintage Umber Shag Carpet",
"Abandoned Roadside Ham Hock",
"Adult Blobfish",
"Ambitious Corn Dog that Escaped from the Concession Stand at a Rural Alabama Fairground, Stole an Unattended Wig, Hopped a Freight Train to Atlantic City and Never Looked Back",
"Angrily Reanimated Christmas Ham",
"Angry Creamsicle",
"Bag of Flour",
"Bag of Toxic Sludge",
"Bewildered, Golden-Helmeted Astronaut Who’s Just Landed on This Planet from a Distant Galaxy",
"Billionaire and Presidential Nominee Who Inexplicably Believes the World is Set Against Him",
"Blackening Scab Artfully Hiding in Your Raisin Bran",
"Bone-in Ham",
"Brightly Burning Trash Fire",
"Bursting Landfill of Municipal Solid Waste",
"Candied Yam Riddled with Moldy Spider Carcasses",
"Carnivorous Plant Watered with Irradiated Bat Urine",
"Cartoon Representation of Irritable Bowel Syndrome in a Pharmaceutical Ad",
"Cheeto Jesus",
"Cheeto-Dusted Bloviator",
"Cheeto-Faced Ferret",
"Chester Cheetah Impersonator",
"Class Clown that Everyone Wishes Would Be Quiet and Let The Class Learn",
"Cryogenically Frozen Bog Man",
"Day-Glo Roadside Billboard About Jock Itch",
"Decomposing Ear of Corn",
"Decomposing Jack-O-Lantern",
"Decomposing Pumpkin Pie Inhabited by Vicious Albino Squirrels",
"Deflated Football",
"Disappointment",
"Disgraced Racist",
"Dishrag that on Closer Inspection is Alive with Maggots",
"Dusty Barrel of Fermented Peepee",
"Empty Popcorn Bag Rotting in the Sun",
"Enlarged Pee-Splattered Sno Cone",
"Enraged Gak Spill",
"Enraged, Bewigged Fetus Blown up to Nightmarish Size",
"Fart-Infused Lump of Raw Meat",
"Fiberglass-Topped Tantrum Thrower",
"Figurative Rubber, and also Literal Rubber",
"Flatulent Leather Couch",
"Fossilized Meatball",
"Four-Time Bankruptcy Filer and Seething Hernia Mass",
"Frequent Provider of Unsolicited Judgements Regarding Female Attractiveness",
"Full-Grown Monopoly Dog Carefully Balancing a Spongecake Atop His Head",
"Future Leader of the Free World",
"Fuzzy Meat-Wad",
"Gaffe-Prone Lunatic",
"Gangrenous Gaping Wound",
"Gender-Threatened Lead Paint Factory Explosion",
"Glistening, Shouting Gristle Mass with a History of Saying Terrible and Stupid Things",
"Great Judgement-Haver",
"Hair Fuehrer",
"Hair Plug Swollen with Rancid Egg Whites",
"Hair That You Pluck, Causing a Cluster of Hairs to Sprout in Its Place",
"Hairpiece Come to Life",
"Harkener to Unspecified Moment of American Greatness",
"Heaving Carcass",
"Horking Mole-Creature Suffering from Radioactive Spray-Tan",
"Horsehair Mattress Stuffed with Molding Copies of Hustler",
"Human Equivalent of Cargo Pants that Zip Away into Shorts",
"Human Kinder Egg Whose Inner Surprise is a Tiny Pebble of Rat Shit",
"Human-Shaped Wad of Gak",
"Human-Sized Infectious Microbe",
"Human-Toupee Hybrid",
"Human/Komodo Dragon Hybrid",
"Idiot Magnet",
"Idiot Media Savant",
"Inside-Out Lower Intestine",
"KKK Rally Port-a-Potty Holding Tank",
"Lamprey Eel Spray-Painted Gold",
"Lead Paint Factory Explosion",
"Little Gloves",
"Lumbering Human-Life Tardigrade",
"Malfunctioning Wind Turbine",
"Malignant Corn Chip",
"Man Who Cherishes Women",
"Man Who Could One Day Become the First Hobgoblin to Enter The White House",
"Man with the Hair of a Radioactive Skunk",
"Man-Baby",
"Man-Shaped Asbestos Insulation Board",
"Man-Sized Sebaceous Cyst",
"Mangled Apricot Hellbeast",
"Master of Zero-Sum Business Deals",
"Melting Businessman",
"Melting Pig Carcass",
"Microwaved Circus Peanut",
"Monument to Human Hubris Crafted out of Rotting Spam",
"Mountain of Rotting Whale Blubber",
"Nacho Cheese Golem",
"Narcissistic Bowl of Rotten Gazpacho",
"National Embarrassment",
"Neo-Fascist Real Estate Golem",
"Neon-Tinted Hellion",
"New Superfood Made of Finely-Ground Clown Wigs",
"Normal-Looking Human Man and Entirely Credible Choice as Future Leader of the Free World",
"Noted Troll",
"Numpty",
"Orange Muppet",
"Oversized Wasp Exoskeleton Stuffed with Old Mustard",
"Own Best Parody",
"Pair of Chapped Lips Superglued to a Hairball",
"Parental Pile of Burnt Organic Material",
"Play-Doh Factory Explosion",
"Plentiful Field of Dung Piled into the Shape of a Presidential Candidate",
"Pond Scum",
"Poorly-Drawn Fascist",
"Poorly-Trained Circus Organgutan",
"Presidential Candidate and Bargain Bin Full of Yellowing Jean-Claude Van Damme Movies",
"Purveyor of Lousy Steak",
"Racist Teratoma",
"Racist, Sexist Block of Aged Cheddar",
"Rage Tribble",
"Real-Estate Tycoon with Simple, Stupid Plan to Defeat ISIS",
"Republican Babadook",
"Republican Frontrunner and 250-pound Accumulation of Rancid Beef",
"Rich Idiot Willing to Allow Garbage to Fall Out of His Mouth Without Batting a Single Golden Lash",
"Roiling Cheez Whiz Mass",
"Rumpelstiltskin Inflated with a Bike Pump and Filled with Bacteria",
"Scab You Wish You Hadn't Picked",
"Screaming Giant Cheese Wedge",
"Seagull Dipped in Tikka Masala",
"Seeping Fleabag",
"Self-Proclaimed Ponderer of Incest",
"Self-Tanning Enthusiast",
"Sentient Hate-Balloon",
"Sentient Waste Disposal Plant",
"Serial Propogator of Demonstrable Falsehoods",
"Short-Findered Vulgarian",
"Shriveled Pinto Bean You Had to Pluck out of Your Chipotle Burrito Basket",
"Sloshing Styrofoam Takeout Container Filled with Three-Day-Old Mac and Cheese",
"Soggy Burlap Sack",
"Sputum-Filled Orange Julius",
"Stately Hot Dog Casing",
"Sticky, Grabby, Cheeto-Hued Toddler with No Sense of Adult Deportment",
"Sun-Dried Tomato",
"Sunken, Corroding Soufflé",
"Swollen Earthworm Gizzard",
"Talking Comb-Over",
"Talking Dingleberry",
"Tattered Craigslist Sofa",
"Temperamental Gelatinous Sponge",
"The Kindest, Bravest, Warmest, Most Wonderful Human Being You'll Ever Know in Your Life",
"The Sculpture your Three-Year-Old Made but of Soggy Ground-Up Goldfish Snacks",
"Tiny Piece of Dried Cat Poop that You Found in Your Rug",
"Traditional Values Adulterer with Two Ex-Wives",
"Ugly Racist",
"Unconvincing Presidential Simulation",
"Uncooked Chicken Breast",
"Undead Tangerine",
"Unkempt Troll Doll Found Floating Facedown in a Tub of Rancid Beluga Caviar",
"Unrepentant Birther",
"Used Q-tip",
"Usually Reasonable Burlap Sack Full of Rancid Peeps",
"Walking Faux Luxury Brand",
"Walking Irradiated Tumor",
"Walking Pile of Reanimated Roadkill",
"Wall Construction Expert",
"Wart We Can't Freeze Off Until November",
"Wax Museum Figure on a Very Hot Day",
"Wealthy Inheritor Disguised as Successful Businessman",
"Weapons-Grade Plum",
"Weirdly Authoritarian Gingerbread Man",
"Yellowing Hunk of Masticated Gristle",
"Your Next President and Ruler for Life",
"“Taco truck”",
];

