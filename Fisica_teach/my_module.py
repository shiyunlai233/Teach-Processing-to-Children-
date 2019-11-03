def set_fbody(fbody, pos=None, v=None, f=None, dens=None, damp=None, 
                  rest=None, fric=None, stroke=None, fill=None, img=None):
    if pos:
        fbody.setPosition(*pos)
    if v:
        fbody.setVelocity(*v)
    if f:
        fbody.setForce(*f)
    if dens:
        fbody.setDensity(dens)
    if damp:
        fbody.setDamping(damp)
    if rest:
        fbody.setRestitution(rest)
    if fric:
        fbody.setFriction(fric)
    if stroke:
        fbody.setStroke(*stroke)
    if fill:
        fbody.setFill(*fill)
    if img:
        fbody.attachImage(img)
