files = """Abilities/AbilityDetector.yml
Abilities/AntiBowStar.yml
Abilities/AntiFall.yml
Abilities/AntiTrapRod.yml
Abilities/AntiTrapper.yml
Abilities/Backpack.yml
Abilities/Backstab.yml
Abilities/Beacon.yml
Abilities/Berserk.yml
Abilities/Birds.yml
Abilities/BowTeleport.yml
Abilities/CobwebInvader.yml
Abilities/Combo.yml
Abilities/ComboFlower.yml
Abilities/Decapitator.yml
Abilities/EffectDisabler.yml
Abilities/EffectStealer.yml
Abilities/ExplosiveEgg.yml
Abilities/FairFight.yml
Abilities/FakeLogger.yml
Abilities/FakePearl.yml
Abilities/FocusMode.yml
Abilities/FreezeGun.yml
Abilities/Ghost.yml
Abilities/GodMode.yml
Abilities/Grappling.yml
Abilities/GuardianAngel.yml
Abilities/Harpon.yml
Abilities/HastyRecovery.yml
Abilities/HelmetRemover.yml
Abilities/HopperAbility.yml
Abilities/Hungry.yml
Abilities/HyperTank.yml
Abilities/InvisibleEvasor.yml
Abilities/JumpBoost.yml
Abilities/Katana.yml
Abilities/KitSnipe.yml
Abilities/KitSwapper.yml
Abilities/Larrys.yml
Abilities/MedKit.yml
Abilities/Minions.yml
Abilities/Ninja.yml
Abilities/OpSwitchStick.yml
Abilities/Paralyzer.yml
Abilities/PocketBard.yml
Abilities/PoisonGas.yml
Abilities/PortableBard.yml
Abilities/PortableWitch.yml
Abilities/RageBall.yml
Abilities/RageIngot.yml
Abilities/RageOfRaider.yml
Abilities/RageShocking.yml
Abilities/RealityStone.yml
Abilities/Refill.yml
Abilities/Regeneration.yml
Abilities/Resistance.yml
Abilities/Rocket.yml
Abilities/SafeHandicap.yml
Abilities/SafetyNet.yml
Abilities/Scrambler.yml
Abilities/SelfPull.yml
Abilities/SnowBall.yml
Abilities/Speed.yml
Abilities/SpiderTail.yml
Abilities/Strength.yml
Abilities/SwapperAxe.yml
Abilities/Switcher.yml
Abilities/TheEyesOfSlade.yml
Abilities/ThorHammer.yml
Abilities/TimeGem.yml
Abilities/TimeMachine.yml
Abilities/TimeRock.yml
Abilities/TimeWarp.yml
Abilities/Ultimate.yml
Abilities/UltimateArcherBow.yml
Abilities/Zeus.yml
Abilities/AntiDropdown.yml
Abilities/FastPearl.yml
Abilities/OpExoticBone.yml
Abilities/SwitchStick.yml
Abilities/PotCounter.yml"""

replaced = 0
store = "store.vexpvp.club"
domain = "vexpvp.club"

for file in files.split('\n'):
	with open(file, 'r') as f:
		content = []
		f = f.readlines()
		for line in f:
			if "skilled-dev.club" in line:
				content.append(line.replace('skilled-dev.club', domain))
				replaced+=1
				print(replaced)
			elif "store.youserver.com" in line:
				content.append(line.replace('store.youserver.com', store))
				replaced+=1
				print(replaced)
			else:
				content.append(line)
		with open(file, 'w') as f:
			for line in content:
				f.write(line)
