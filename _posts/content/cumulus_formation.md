

In the previous section, we discussed a basic model of radiative energy transfer. This post is about how cumulus clouds form.

## Dry static energy

We start with the abstraction of a parcel of air. There are certain conserved quantities, like the mass of $O_2$. An example of a quantity that is not conserved is heat. Imagine a parcel of air that has an average temperature of $298K$ sitting in an environment with average temperature of $280K$ will eventually equilibriate. The reason we care is that "mixing" homogenizes conserved variables.

<!-- I’m not actually sure what we mean by mixing will homogenize conserved variables means. If we were in some simple world with no pressure, radiation, vapors, wouldn’t the temperature eventually homogenize. Conservation in the sense that $DQ/Dt = 0$, where $Q$ is the quantity in question. So the total flux of the quantity to/from the parcel is zero. I guess the idea is to keep track of parcel properties as they move around. -->

$$ \rho\frac{D}{Dt}(c_{\text{air}}T) = \frac{DP}{Dt} + L_{\text{water}}C + Q_{\text{rad}} $$

Glossary of terms:
 * $D/Dt$: The Lagrangian ("total") derivative with respect to time. Contrast this with the partial derivative of a quantity.
 * $c_{\text{air}}T$: The enthalpy of the parcel, which is the total energy required to create the system: forming the molecular bonds, positioning the formed molecules, displacing the environment for it to be where it is. $c_{\text{air}}$ is the specific heat of air, and $T$ is the temperature.
 * $P$: The pressure of (on?) the parcel.
 * $L_{\text{water}}C$: The rate at which heat enters the system from condensation. $L_{\text{water}}$ is the latent heat of condensation of water, or the amount of heat per unit of water condensed. $C$ is the actual condensation rate. In particular, the represents the energy released when water undergoes a phase transition from gas to water, and not the temperature changes needed to reach these phase transitions.
 * $Q_\text{rad}$: The rate that heat enters the system via radiation.

In practice, pressure changes > condensation changes > radiation in terms of total heat transfer. (include the numbers provided in the chapter)

As you can see from this differential equation, temperature is not a conserved quantity. So if we can safely ignore any condensation or radiation effects, we can introduce a quantity called the dry static energy:

$$s = c_{\text{air}}T + gz,$$

where $g$ is the gravitational constant and $z$ is the altitude. Each term has units of $J\cdot \text{kg}^{-1}$; the first term is the enthalpy and the second is the potential energy, per unit mass of the parcel.

There is an intimate relation between the altitude and the pressure. The pressure is the force per unit area on a parcel of air. Swimming pool analogy. Thus the marginal weight difference as altitude is varied is:

$$ \frac{dP}{dz} = -\rho g$$

The negative sign is a convention to indicate that the pressure decreases as the altitude increases. Thus, when a parcel of air increases in altitude, it will expand due to having less pressure and thereforme its temperature will drop. No matter how effective the turbulent mixing, temperature alone can never be homogenized through mixing.

*Exercise*: Show that $\frac{Ds}{Dt} = L_{\text{water}}C + Q_{\text{rad}}$.

<!-- Another thing to clarify: $\rho g$ looks like the buoyant force constant. Is this the buoyant force, or is it different? -->

If we look at the actual DSE levels with respect to altitude, we get:

![dry static energy](/assets/cumulus/dry_static_energy.png){:.center-image}

The DSE curve is divided by $c_{\text{air}}$ to give units of temperature. As you can see, DSE is increases strongly with height. Does this contradict the principle that DSE is conserved as a parcel of air varies in altitude? No. This plot represents the equilibrium distribution of DSE. A parcel of air that starts will higher DSE than its environment will have higher temperature than the air around it. Buoyant forces will act on the parcel of air to move it higher, decreasing the parcel’s temperature but increasing its altitude. The parcel’s DSE is still conserved, and "organized" at the appropriate altitude according to this quantity. This means that air will have a tendency to maintain its relative vertical position, and all turbulent behavior will act on the air horizontally.

Another way of capturing this idea is to look at the lapse rate, the rate at which the temperature decreases with altitude (the negative "acceleration" of temperature). For lstratified layers to form, the lapse rate $\Gamma$ of the surrounding air must be lower than the lapse rate of the dry air parcel $\Gamma_d$. Consider a warm air parcel in a cooler environment. After being lifted $1 \text{km}$ by buoyant forces, the temperature difference drops a little, density differential also decreases so the buoyant force is a little weaker. Eventually, the buoyant force converges to $0$.

Let’s do a rough calculation for a parcel of air at 10 km. This has a temperature of roughly $220K$. If this parcel of air were moved to ground level, the change in temperature is $10^4 \text{m} \cdot 10 \tfrac{\text{m}}{\text{s}^2} \cdot (10^3 \tfrac{\text{J}}{\text{kg}\cdot \text{K}} \cdot \rho)^{-1} = 100K$, so the parcel of air would be $320K$ or $47 C$ at ground level, pretty hot by human standards. This is consistent with our expectations that warmer air rises.

The DSE doesn’t always increase with altitude. (Think a hot parking lot, where the surface is hotter.)

## Moist Static Energy

The previous analysis assumes that no energy is lost or gained through water vapor condensation. Let’s factor that in now. Once again, our motivation is to define a quantity, called the moist static energy (MSE), which is conserved with altitude and phase transition changes:

$$ h = c_{\text{air}}T + gz + L_\text{water}q $$

The quantity $q$ represents the specific humidity, given by $q = \frac{\rho_{\text{vapor}}}{\rho}$. You can also think of this term as the fraction of the parcel’s mass which is water vapor. Importantly, $q$ satisfies:

$$ \rho \frac{Dq}{Dt} = -C,$$

where $C$ is the condensation rate we saw earlier. When $C<0$, this represents evaporation. We can use this to show the definition of MSE is equivalent to moving the $LC$ term to the left-hand side of the heat equation: $\frac{Dh}{Dt} = Q_{\text{rad}}$.

Evaporation occurs when water molecules on the surface of a liquid move fast enough to escape it. Likewise, condensation occurs when water vapor hits and merges back into the liquid. For a reason I don’t fully understand, this balance between evaporation and condensation is dictated by the external vapor pressure. The vapor pressure when these two are in equilibrium is the saturation vapor pressure, which exponentially increases with temperature. For example, in the tropics near the ocean, we experience very humid climates. 

In this sense, the saturation vapor pressure represents the maximum vapor pressure a parcel of air at that temperature can contain. If the relative humidity $e^{\star}$, the ratio of partial pressure of water vapor to the saturation vapor pressure, exceeds $1$, then water begins to condense. Unless it is very cold, it is rare to have $e^{\star}$ exceed $1$ by more than a little bit.

This allows us to also define the saturation specific humidity $q^\star$, the corresponding specific humidity at saturation levels, and the saturation MSE $h^\star = c_\text{air}T + gz + L_\text{water}q^\star$. If we plot DSE, MSE, and saturation MSE together at a typical rainy tropical location, we have:

![moist static energy](/assets/cumulus/moist_static_energy.png){:.center-image}

Remember that these are energy levels of the surrounding air. We can make a few observations out of this. First, the MSE at a given height is always less than the saturation MSE. This makes sense, as $q \le q^\star$ at all points. As a result, MSE increases with altitude for the same reasons as DSE.

Furthermore, at higher altitudes, all three plots more or less converge to the same curve. Here, the governing law is that the concentration of water decreases exponentially with altitude. (Chapter 1) Water vapor condensation does not play a large role at these higher altitudes because there’s simply less of it. 

Conversely, at lower altitudes, the concentration of water vapor is very high. Because the total latent heat (heat carried by the water vapor) is highest at low altitudes, the total MSE actually decreases with altitude close to the ground. This means that we have a local minimum for MSE somewhere in the middle troposphere. A similar thing can be said about the saturation MSE curve.

This minimum is significant. Consider a parcel of air with MSE of $347 \text{ kJ}/\text{kg}$. MSE is conserved as it traverses different altitudes, so the vertical line represents this parcel’s $(MSE, z)$ states. If the parcel’s MSE is higher than saturation MSE of the surrounding air (i.e. above the level of free convection (LCE)), then since we know that $q \le q^\star$ and $z_\text{parcel} = z_\text{surroundingAir}$, then the parcel’s temperature is also higher than the surrounding air’s. Hence, it will be lifted by buoyant forces.

What happens as this parcel rises? First, the parcel’s water vapor condenses, since it exceeds saturation levels. Remember that the MSE is still conserved because it takes this condensation effect into account. Second, the temperature decreases due to decreased pressure. This checks out with our assumption that MSE is conserved; as the parcel’s potential energy increases, its enthalpy and latent heat decrease. 

This process happens until it hits the level of neutral buoyancy. The parcels accumulating at this altitude explains the anvil-shape of the clouds.

![Anvil shape of clouds](/assets/cumulus/cumulus_anvil.jpg){:.center-image}

You might wonder, when the water vapor condenses, doesn’t the water fall and "leave" the parcel? The answer is yes! If a parcel of air starts near the lower troposphere, it is much faster for the parcel to reach the upper atmosphere than it is to return to its original altitude, because it cannot re-evaporate the water it lost. Parcels in the upper atmosphere lose heat via radiation to space, allowing it to come down slowly. It still conserves MSE, but with a different distribution of enthalpy, potential energy, and latent heat than it started with, and at a much slower rate.

Let’s compare a moist parcel to its surrounding air in saturation conditions. With a unit increase in altitude, both gain equivalent amounts in potential energy. However, because saturation capacity decreases with altitude (why?), some of the parcel’s water vapor condenses, so it loses latent heat and gains enthalpy in saturation conditions, relative to the surrounding air. Thus, $\Gamma_w < \Gamma < \Gamma_d$. Contrasting this with dry static conditions, this means that the air parcel actually accelerates on its way up.

Just to appreciate this process, consider a cooler parcel of air with MSE of $335 \text{ kJ}/\text{kg}$ instead. Unlike the warmer parcel in our previous example, the cooler parcel never reaches saturation humidity, regardless of altitude. Thus, it will be stratified according to temperature like in the DSE case; the highly humid air parcels can be at any altitude. Contrasting this with the warmer parcel, condensation effects cause highly moist air to rise and accumulate to similar heights, creating a cloud.

![moist static energy](/assets/cumulus/moist_static_energy_335.png){:.center-image}

<!-- What happens if it starts below the LCE? Stratified, by same reasoning as DSE? Or since it’s higher than the base MSE of surrounding air, it will rise? -->

## Sources

This post mirrors Chapter 3 of *Atmosphere, Clouds, and Climate* by David Randall, with lots of helpful discussion with Minmin Fu.









