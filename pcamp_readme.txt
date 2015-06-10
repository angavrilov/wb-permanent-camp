Features:

  * Leave a companion to command a permanent camp near a center for a small sum.

    - Garrison size is limited to player party size + commander skill bonus.
    - Prisoner count is limited based on commander skill + garrison troop count.
    - Troops draw full wage, but are assumed to buy their own food from locals.
    - Can store items, which increases bandit attraction.

  * Camps can and will be attacked by hostile parties.

    - All stored items are lost if camp is destroyed.
    - If defeated, companion will return to party unless imprisoned by a lord.
    - Camp will join in the battle if player is attacked right on top of it.
    - Player will stop resting and join battle if current camp is attacked.

Bugs:

  * Camps are ordinary parties told to stay put, but they technically can still move
    if AI decides to for some reason. Haven't seen this after a few tweaks though.

  * Camp interactions leave spurious battle marks that can be seen with tracking
    skill after disbanding the camp.

  * AI is unaware that camps will always join in on the battle and can be easily
    tricked into attacking against the odds.

  * Camp troops in battle have no banner (but still obey player commands).
