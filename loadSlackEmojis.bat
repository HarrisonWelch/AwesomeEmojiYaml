REM loadSlackEmojis.bat

echo HELLO, WORLD!

REM for %%r in ("https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/avengers.yaml" 
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/businessfish.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/clippy.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/fika.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/finland.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/food.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/frontend.yaml") do (

REM for %%r in ("https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/futurama.yaml" 
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/german-states.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/harrypotterhouses.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/mario-8bit.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/nekoatsume.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/occupy.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/officespace.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/omnom.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/parrotparty.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/pokemongo.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/politipack.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/shiba.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/skype.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-facebook-reaction.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-logo.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-meme.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-mlb.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nba.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nfl.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nhl.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nyc-subway.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-party-parrot.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-pokemon.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-retro-game.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-scrabble-letters.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-star-wars.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-turntable.fm.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-yoyo.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/startups.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/starwars.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/twitch.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/unicorn.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/weapons.yaml"
REM             "https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/octicons.yaml") do (

REM for %%r in ("https://raw.githubusercontent.com/Templarian/slack-emoji-pokemon/master/pokemon.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/leagueitems.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/leaguechampions.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/web-tech.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/facebook_reactions.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/logos.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/memes.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/nba.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/pokemon.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/retro_games.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/star_wars.yaml"
REM             "https://raw.githubusercontent.com/alexmckenley/emojipacks/master/uncategorized.yaml"
REM             "https://raw.githubusercontent.com/HarrisonWelch/AwesomeEmojiYaml/master/awesome_emoji.yaml") do (

for %%r in ("https://raw.githubusercontent.com/HarrisonWelch/AwesomeEmojiYaml/master/awesome_emoji.yaml") do (
   echo %%r
   https://raw.githubusercontent.com/HarrisonWelch/AwesomeEmojiYaml/master/awesome_emoji.yaml
   emojipacks -s <slack domain> -e <email> -p <password> -y %%r
)
