def odeint(f, y0, t, args, Dfun=None, integrator='dop853', **kwargs):
    """Provides a odeint-like wrapper around the other ode routines from scipy."""
    def f_ode(t, y):
        return f(y, t, *args)
    integrator = ode(f_ode, jac=Dfun)
    integrator.set_integrator(integrator, **kwargs)
    integrator.set_initial_value(y0, t[0])
    ys = np.empty((len(t), len(y0)))
    for i, ti in enumerate(t):
        y = integrator.integrate(ti)
        ys[i] = y
    return ys
