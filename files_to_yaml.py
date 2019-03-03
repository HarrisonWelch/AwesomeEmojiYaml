# files_to_yaml.py

if __name__ == "__main__":
  print("hello")

  folders = [
    'adventuretime',
    'fallout',
    'futurama',
    'hamsterdance',
    'it-crowd',
    'loading',
    'logos',
    'mario',
    'misc-animals',
    'misc-gaming',
    'misc-memes',
    'misc',
    'miyazaki',
    'overwatch',
    'pokemon',
    'ragefaces',
    'rick-and-morty',
    'steven-universe',
    'world-of-warcraft',
    'zelda',
  ]

  files = [
    ['banana-guard.png',
    'bmo-dance.gif',
    'bmo-dancing.gif',
    'bmo-love.gif',
    'cupcake-flex.png',
    'dancing-baby-finn.gif',
    'excited-fin.gif',
    'finn_dance.gif',
    'happy-bmo.gif',
    'hmmmmn.gif',
    'iceking.gif',
    'jake-blink.gif',
    'jake-heart.gif',
    'jake-wag.gif',
    'lady-rainacorn.png',
    'lemongrabplz.gif',
    'lsp-puke-rainbows.gif',
    'lsp.gif',
    'mr_cupcake.png',
    'pb-and-pep.gif',
    'pb.png',
    'pb2.png',
    'pb3.png',
    'pb4gif.gif',
    'penguin-love.gif',
    'pep.gif',
    'slime-princess.gif',
    'slime.gif',
    'snail-wave.gif',
    'sparkly-finn-jake.gif',
    'starchy.png',
    'stretchy-jake.gif',
    'susan-strong.png',
    'treetrunks-pie.gif',
    'treetrunks.png',
    'wahwahwah.gif',
    'winking-jake.gif',
      ],[
    'fallout-nuka-cola.png',
    'fallout-nuka_cola-bottle.png',
    'fallout-ok.png',
    'fallout-pip-boy.png',
    'fallout-thirst-zapper.png',
    'fallout-trophy.png',
      ],[
    'bender-banana.gif',
    'bender-dance.gif',
    'bender-getdown.gif',
    'fry-dance.gif',
    'fry-headspin.gif',
    'fry-walk.gif',
    'futurama_zoidbergSeppuku.gif',
    'happy-leela.gif',
    'hypnotoad.gif',
    'hypnotoad2.gif',
    'leela_amy_wrestling.gif',
    'zoiberg.gif',
    'zoidberg-scuttle.gif',
      ],[
    '2.gif',
    'HamsterDances.gif',
    'anin-ham.gif',
    'anin.gif',
    'hampsterdancegame-hat.gif',
    'hamsterdance-grey-single.gif',
    'hamsterdance.gif',
    'hamsterdance.gif-c200.gif',
    'hamsterdance2.gif',
    'hamsterdance3.gif',
      ],[
    'jen.png',
    'moss-bw-partial.png',
    'moss-bw.png',
    'moss-cheer.png',
    'moss.jpg',
    'moss.png',
    'roy.png',
      ],[
    'bbod.gif',
    'loading-plz.gif',
    'loading.gif',
      ],[
    'android.png',
    'apple_logo.jpg',
    'aws-logo.png',
    'coffeescript.png',
    'defcon.png',
    'golang.png',
    'heroku.png',
    'microsoft_logo_2012.png',
    'perl.gif',
    'php.png',
    'python.png',
    'ruby.png',
      ],[
    'Coin-Pip.gif',
    'Coin.gif',
    'Goomba.gif',
    'Question_Block.gif',
    'Smilie_v2_Luigi.gif',
    'plant.gif',
    'supermariowalkright.gif',
    'toad.gif',
      ],[
    'dodo.png',
    'platypus.png',
    'raccoon.png',
      ],[
    'donkey-kong.gif',
    'game.png',
    'nes.png',
    'nes2.png',
    'pvz-sad-zombi.png',
      ],[
    'allthethings.png',
    'badgerbadgerbadger.gif',
    'dickbutt.jpg',
    'doge.png',
    'goatse.gif',
    'grumpy-cat.png',
    'haterade.jpg',
    'leftshark-dance.gif',
    'llap.png',
    'nyan.gif',
    'old-man-yells-at-cloud.jpg',
    'picard-facepalm.jpg',
    'sir.png',
      ],[
    '75.gif',
    'Octocat.png',
    'censored.gif',
    'cheer.gif',
    'cockroach.png',
    'flying-brain.gif',
    'icon_rtfm.gif',
    'mf.png',
    'pistol.gif',
    'ranchmoji.gif',
    'rtfm-sign.gif',
    'signs-mug.gif',
    'voodoo.gif',
    'whiskey.jpg',
      ],[
    'calcifer.gif',
    'forest-spirit.gif',
    'happy-sootsprite.gif',
    'no-face.gif',
    'soot-sprites.gif',
    'sprite.gif',
    'totoro-hoop.gif',
    'totoro.gif',
      ],[
    'Mei.png',
    'Widowmaker.png',
    'ana.png',
    'birgitta.png',
    'dad-76-waist.png',
    'genji.png',
    'hanzo.png',
    'junkrat.png',
    'logo.png',
    'lucio.png',
    'mercy-2.png',
    'mercy.png',
    'moira.png',
    'orisa.png',
    'overwatch-ana.png',
    'overwatch-bastion.png',
    'overwatch-dva.png',
    'overwatch-genji.png',
    'overwatch-hanzo.png',
    'overwatch-junkrat.png',
    'overwatch-lucio.png',
    'overwatch-mcree.png',
    'overwatch-mei.png',
    'overwatch-mercy.png',
    'overwatch-pharah.png',
    'overwatch-reaper.png',
    'overwatch-reinhardt.png',
    'overwatch-roadhog.png',
    'overwatch-solider-76.png',
    'overwatch-sombra.png',
    'overwatch-symmetra.png',
    'overwatch-torbjorn.png',
    'overwatch-tracer.png',
    'overwatch-widowmaker.png',
    'overwatch-winston.png',
    'overwatch-zarya.png',
    'overwatch-zenyatta.png',
    'pharah.png',
    'reaper-guns.png',
    'reinhardt-waist.png',
    'reinhardt.png',
    'sombra-waist.png',
    'symmetra.png',
    'torbjorn.png',
    'tracer-hips.png',
    'tracer.png',
    'winston.png',
    'zarya.png',
    'zenyatta.png',
      ],[
    'bulbasaur-run.gif',
    'caterpie.gif',
    'charmander-lick.gif',
    'mew-pokeball.gif',
    'ninetails.gif',
    'pika-bounce.gif',
    'pika-run.gif',
    'pika-sleep.gif',
    'pokeball.png',
    'psyduck-lick.gif',
    'raichu.gif',
    'slowpoke.jpg',
    'vulpix-run.gif',
      ],[
    '1.gif',
    '10.gif',
    '100.gif',
    '101.gif',
    '102.gif',
    '103.gif',
    '104.gif',
    '105.gif',
    '11.gif',
    '12.gif',
    '13.gif',
    '14.gif',
    '15.gif',
    '16.gif',
    '17.gif',
    '18.gif',
    '19.gif',
    '2.gif',
    '20.gif',
    '21.gif',
    '22.gif',
    '23.gif',
    '24.gif',
    '25.gif',
    '26.gif',
    '27.gif',
    '28.gif',
    '29.gif',
    '3.gif',
    '30.gif',
    '31.gif',
    '32.gif',
    '33.gif',
    '34.gif',
    '35.gif',
    '36.gif',
    '37.gif',
    '38.gif',
    '39.gif',
    '4.gif',
    '40.gif',
    '41.gif',
    '42.gif',
    '43.gif',
    '44.gif',
    '45.gif',
    '46.gif',
    '47.gif',
    '48.gif',
    '5.gif',
    '6.gif',
    '7.gif',
    '8.gif',
    '9.gif',
      ],[
    'ants-in-my-eyes.png',
    'beth-angry.png',
    'beth-scared.png',
    'beth-serious.png',
    'beth-smile.png',
    'blips-and-chips.png',
    'butter-robot.png',
    'giant-nakes-santa.png',
    'jerry-angry.png',
    'jerry-eyeroll.png',
    'jerry-mansplain.png',
    'jerry-scream.png',
    'jerry-skeptical.png',
    'meeseeks-anguish.png',
    'meeseeks.png',
    'morty-derp.png',
    'morty-heh.png',
    'morty-sad.png',
    'morty-smile.png',
    'pickle-rick.png',
    'portal-gun.png',
    'rick-and-morty-portal.png',
    'rick-drinking.png',
    'rick-hey-2.png',
    'rick-hey.png',
    'rick-panic.png',
    'rick-whatever.png',
    'robo-rick.png',
    'screaming-morty.png',
    'screaming-sun.png',
    'show-me-what-you-got.png',
    'snuffles.png',
    'special-rick.png',
    'summer-angry.png',
    'summer-crying.png',
    'summer-happy.png',
    'szechuan.png',
      ],[
    '8-bit-connie.png',
    '8-bit-garnet.gif',
    'amethyst.png',
    'connie.png',
    'fusion.png',
    'gem.png',
    'happy-amethyst.jpg',
    'lion.png',
    'love.gif',
    'pearl-nope.png',
    'pearl.png',
    'stern-garnet.png',
    'steve-tadah.png',
    'steven-ani.gif',
    'steven-connie-fusion.png',
    'steven-happy-head.png',
    'steven-run.png',
    'steven-shield.png',
    'steven-shouting.png',
    'steven-star.png',
      ],[
    'alliance.jpg',
    'blood-elf.png',
    'chest.jpg',
    'demon-hunter.png',
    'druid.png',
    'horde.png',
    'hunter.png',
    'mage.png',
    'shaman.png',
    'wow-logo.png',
      ],[
    'ArmosKnight(Front).gif',
    'BlueCandle.gif',
    'BlueRing.gif',
    'Fairy.gif',
    'Fire.gif',
    'GelBlack.gif',
    'LifePotion.gif',
    'LifePotion2.gif',
    'Link (Normal) - Red Ring.gif',
    'Link(Normal)(Back).gif',
    'Link(Normal)(Front)1.gif',
    'Link(Normal)(Left)1.gif',
    'Link(Normal)Item1.gif',
    'Link(Normal)Item2.gif',
    'MedicineWoman.gif',
    'Octorok - Blue (Front).gif',
    'Octorok - Red (Front).gif',
    'OldMan.gif',
    'PolsVoice.gif',
    'PrincessZelda.gif',
    'PrincessZeldaTriforce.gif',
    'Rupee.gif',
    'Spiny.gif',
    'TektikeBlue.gif',
    'TektikeRed.gif',
    'WomanRed.gif',
    'ZolGrey.gif',
    'sweat.gif',
    ]
  ]

  ofile = open('awesome_emoji.yaml', 'w')

  spaces = 0

  ofile.write((' '*spaces) + '# awesome_emoji.yaml' + '\n')
  ofile.write((' '*spaces) + '' + '\n')
  ofile.write((' '*spaces) + 'title: awesome' + '\n')
  ofile.write((' '*spaces) + 'emojis:' + '\n')
  
  spaces = 2

  # print("files = " + str(files))

  prefix = 'https://raw.githubusercontent.com/snipe/awesome-emoji/master/'

  for i in range(0, len(folders)):
    print(folders[i])
    for j in range(0, len(files[i])):

      print(files[i][j])

      ofile.write( (' '*spaces) + '- name: ' + files[i][j][:-4] + '\n')

      if files[i][j][0].isdigit():
        print('hey')
        ofile.write( (' '*(spaces+2)) + 'src: ' + prefix + folders[i] + '/' + folders[i] + '_' + files[i][j] + '\n')
      else:
        ofile.write( (' '*(spaces+2)) + 'src: ' + prefix + folders[i] + '/' + files[i][j] + '\n')
        

  print("goodbye")
