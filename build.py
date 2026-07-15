import re, os

ROOT = "/home/claude/portfolio"
PROJ_DIR = os.path.join(ROOT, "projects")
os.makedirs(PROJ_DIR, exist_ok=True)

# ---------------------------------------------------------------
# PROJECT DATA — edit this list to add/remove/reorder projects.
# images: list of paths relative to the site root (media/...).
#         Add more entries here later as you get more photos.
# ---------------------------------------------------------------
PROJECTS = [
    dict(title="Merchant's Hooded Robe", category="game", catLabel="Game Asset",
         images=["media/merchant-robe.jpg"],
         desc="Game-ready hooded robe outfit fitted to a base mannequin, with a woven cloth shader and a stitched leather belt detail at the waist.",
         tools=["Blender", "Substance Painter"]),
    dict(title="Frostbite Blade", category="game", catLabel="Game Asset",
         images=["media/frostbite-blade.jpg"],
         desc="Curved fantasy sword with a frost-worn steel blade and a moss-grown handle, hand-painted for a stylised weathered look.",
         tools=["Blender", "Substance Painter"]),
    dict(title="Sunfire Scimitar", category="game", catLabel="Game Asset",
         images=["media/sunfire-scimitar.jpg"],
         desc="Ornate gold scimitar with a rusted, battle-worn finish and an openwork crescent detail near the tip.",
         tools=["Blender", "Substance Painter"]),
    dict(title="Tactical Sidearm", category="game", catLabel="Game Asset",
         images=["media/tactical-sidearm.jpg"],
         desc="Modern compact pistol with a textured polymer grip and worn-metal slide, modeled and baked for a realistic PBR finish.",
         tools=["Blender", "Substance Painter", "Marmoset"]),
    dict(title="Gilded Commander 1911", category="game", catLabel="Game Asset",
         images=["media/gilded-1911.jpg"],
         desc="Fully gold-plated 1911-style pistol with engraved filigree and mother-of-pearl grip panels, built as a high-value cosmetic variant.",
         tools=["Blender", "Substance Painter"]),
    dict(title="The Last Message — Leather Satchel", category="game", catLabel="Game Asset",
         images=["media/satchel-top.jpg", "media/satchel-back.jpg"],
         desc="Worn leather satchel prop with a branded wax-stamped clasp, stitched edging and a shoulder strap, modeled for a narrative item pickup.",
         tools=["Blender", "Substance Painter"]),
    dict(title="Hollywood Vanity Set", category="arch", catLabel="Architecture",
         images=["media/vanity-set.jpg"],
         desc="Backstage dressing table scene with a bulb-lit mirror arch, velvet drapery and a tufted stool, staged and lit for a warm theatrical mood.",
         tools=["Blender", "Cycles"]),
    dict(title="Stylised Bedroom", category="arch", catLabel="Architecture",
         images=["media/stylised-bedroom.jpg"],
         desc="Cel-shaded bedroom interior with a built-in bookshelf and sunset-lit window, exploring a flat toon-shaded lighting approach.",
         tools=["Blender", "Cycles"]),
    dict(title="Modern Kitchen Interior", category="arch", catLabel="Architecture",
         images=["media/modern-kitchen.jpg"],
         desc="Photoreal corner kitchen build with oak cabinetry, dark tile splashback and an integrated oven, lit with natural daylight.",
         tools=["Blender", "Cycles"]),
    dict(title="Pure Beauty — Product Render", category="custom", catLabel="Custom Work / Ads",
         images=["media/pure-beauty-jar.jpg"],
         desc="Studio-lit cosmetics jar render with custom branding and label, built as a mockup for a client product shoot.",
         tools=["Blender", "Cycles"]),
    dict(title="Sauvage — Product Ad Concept", category="custom", catLabel="Custom Work / Ads",
         images=["media/sauvage-concept.jpg"],
         desc="Fragrance ad concept pairing a glass bottle render with a fighter jet flyby, composited for a bold action-driven campaign look.",
         tools=["Blender", "Cycles", "Compositing"]),
    dict(title="Airbase Fragrance Concept", category="custom", catLabel="Custom Work / Ads",
         images=["media/airbase-fragrance.jpg"],
         desc="Alternate fragrance ad concept set against a desert airbase backdrop, exploring a more rugged, cinematic product placement.",
         tools=["Blender", "Cycles", "Compositing"]),
    dict(title="Synthwave Skyline", category="custom", catLabel="Custom Work / Ads",
         images=["media/synthwave-skyline.jpg"],
         desc="Retro synthwave cityscape with a chrome sedan on a reflective highway, built around a saturated sunset palette and mirrored water.",
         tools=["Blender", "Cycles", "Compositing"]),
    dict(title="Night City Flyover", category="custom", catLabel="Custom Work / Ads",
         images=["media/nightcity-flyover.jpg"],
         desc="Aerial cyberpunk street scene lined with animated billboards and traffic, built to explore dense neon-lit city composition.",
         tools=["Blender", "Cycles"]),
    dict(title="Night City — HUD Overlay", category="custom", catLabel="Custom Work / Ads",
         images=["media/nightcity-hud.jpg"],
         desc="First-person cyberpunk skyline shot with a UI/HUD overlay pass, framing a distant tower billboard through a vehicle window.",
         tools=["Blender", "Cycles", "Compositing"]),
    dict(title="Warzone Skyline", category="custom", catLabel="Custom Work / Ads",
         images=["media/warzone-skyline.jpg"],
         desc="Silhouetted ruined cityscape under a burning orange sky, with a fighter jet passing overhead — a mood study in scale and atmosphere.",
         tools=["Blender", "Cycles", "Compositing"]),
    dict(title="Missile Strike — Ocean Chase", category="custom", catLabel="Custom Work / Ads",
         images=["media/missile-chase.jpg"],
         desc="Dynamic low-altitude missile shot skimming the ocean surface, built around motion blur and spray effects for a high-speed feel.",
         tools=["Blender", "Cycles", "Compositing"]),
    dict(title="Mesh Simplification Addon", category="technical", catLabel="Technical / R&D",
         images=[],
         desc="Blender Python addon implementing Vertex Clustering, Edge Collapse and QEM decimation, benchmarked for 3D-print infill efficiency.",
         tools=["Python", "Blender API"]),
]

def slugify(title):
    s = title.lower()
    s = s.replace("&", "and")
    s = s.replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

for p in PROJECTS:
    p["slug"] = slugify(p["title"])

print(f"{len(PROJECTS)} projects loaded.")
for p in PROJECTS:
    print(" -", p["slug"], f"({len(p['images'])} imgs)")

# ---------------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------------

HEAD = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_path}">
"""

HEADER = """<header>
  <div class="wrap nav">
    <a href="{home}" class="brand">YOUR NAME<span>.</span></a>
    <nav>
      <ul>
        <li><a href="{home}#work">Work</a></li>
        <li><a href="{home}#process">Process</a></li>
        <li><a href="{home}#contact">Contact</a></li>
      </ul>
    </nav>
    <a class="cv-btn" href="#" id="cvLink">Download CV</a>
  </div>
</header>
"""

FOOTER = """<footer id="contact">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <h2 class="footer-title">Have a project in mind? I'm open to freelance work.</h2>
        </div>
        <div class="footer-links">
          <a href="mailto:youremail@example.com">youremail@example.com</a>
          <a href="#">ArtStation &#8599;</a>
          <a href="#">LinkedIn &#8599;</a>
          <a href="#">GitHub &#8599;</a>
        </div>
      </div>
      <div class="foot-meta">
        <span>&copy; 2026 YOUR NAME</span>
        <span>Built with a blueprint, not a template.</span>
      </div>
    </div>
  </footer>
"""

BG_LAYERS = """<div class="bg-drift"></div>
<div class="bg-letters" id="bgLetters"></div>
"""

def js_str_array(items):
    return "[" + ", ".join('"' + i.replace('"', '\\"') + '"' for i in items) + "]"

# ---------------------------------------------------------------
# INDEX.HTML
# ---------------------------------------------------------------

projects_js = "const PROJECTS = [\n"
for p in PROJECTS:
    tools_js = js_str_array(p["tools"])
    images_js = js_str_array(p["images"])
    desc_js = p["desc"].replace('"', '\\"')
    title_js = p["title"].replace('"', '\\"')
    projects_js += f'''  {{
    slug: "{p["slug"]}",
    title: "{title_js}",
    category: "{p["category"]}",
    catLabel: "{p["catLabel"]}",
    images: {images_js},
    desc: "{desc_js}",
    tools: {tools_js}
  }},
'''
projects_js += "];\n"

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD.format(title="Portfolio — 3D Artist & Technical Generalist", css_path="styles.css")}
</head>
<body>

{BG_LAYERS}
<a href="#work" class="skip-link">Skip to work</a>

{HEADER.format(home="#top")}

<main id="top">
  <section class="hero wrap">
    <div class="eyebrow">3D Generalist — Hard Surface &amp; Environment</div>
    <h1>Assets built for <em>games</em>, spaces built for <em>living</em>.</h1>
    <p class="hero-sub">I model, retopologize, and texture — from character clothing and weapons for shipped game projects, to architectural interiors and cinematic renders. Everything below moved through a full high-to-low poly pipeline.</p>
    <div class="spec-strip">
      <div>
        <div class="spec-label">Focus</div>
        <div class="spec-value">Game assets &middot; ArchViz</div>
      </div>
      <div>
        <div class="spec-label">Tools</div>
        <div class="spec-value">Blender &middot; Substance</div>
      </div>
      <div>
        <div class="spec-label">Availability</div>
        <div class="spec-value">Open to freelance</div>
      </div>
    </div>
  </section>

  <section class="section wrap" id="work">
    <div class="section-head">
      <h2 class="section-title">Selected Work</h2>
      <span class="section-num mono">DRAWING SET — {len(PROJECTS):02d} SHEETS</span>
    </div>

    <div class="filters" id="filters">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="game">Game Assets</button>
      <button class="filter-btn" data-filter="arch">Architecture</button>
      <button class="filter-btn" data-filter="custom">Custom Work / Ads</button>
      <button class="filter-btn" data-filter="technical">Technical</button>
    </div>

    <div class="grid" id="grid"></div>
  </section>

  <section class="section wrap" id="process">
    <div class="section-head">
      <h2 class="section-title">Pipeline</h2>
      <span class="section-num mono">01 &#8594; 05</span>
    </div>
  </section>
  <div class="process wrap" style="max-width:1180px; margin:0 auto 80px; padding:0 32px;">
    <div class="step"><div class="step-num">01</div><div class="step-title">High-poly sculpt</div><div class="step-desc">Form and detail established without topology constraints.</div></div>
    <div class="step"><div class="step-num">02</div><div class="step-title">Retopology</div><div class="step-desc">Clean, deformation-ready mesh built to a target poly budget.</div></div>
    <div class="step"><div class="step-num">03</div><div class="step-title">UV layout</div><div class="step-desc">Efficient unwraps, minimized seams and texel density checks.</div></div>
    <div class="step"><div class="step-num">04</div><div class="step-title">Bake</div><div class="step-desc">Normal, AO and curvature maps transferred from high to low poly.</div></div>
    <div class="step"><div class="step-num">05</div><div class="step-title">Texture &amp; deliver</div><div class="step-desc">PBR texturing, engine-ready export, turntable render.</div></div>
  </div>

  {FOOTER}
</main>

<script>
{projects_js}
</script>
<script src="background.js" defer></script>
<script src="cards.js" defer></script>
</body>
</html>
"""

with open(os.path.join(ROOT, "index.html"), "w") as f:
    f.write(index_html)

print("index.html written.")

# ---------------------------------------------------------------
# PROJECT PAGES
# ---------------------------------------------------------------

for idx, p in enumerate(PROJECTS, start=1):
    images_rel = ["../" + img for img in p["images"]]
    images_js = js_str_array(images_rel)
    title_js = p["title"].replace('"', '\\"')
    tools_chips = "".join(f'<span class="chip">{t}</span>' for t in p["tools"])

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD.format(title=p["title"] + " — Portfolio", css_path="../styles.css")}
</head>
<body>

{BG_LAYERS}

{HEADER.format(home="../index.html")}

<main>
  <section class="project-hero wrap">
    <a href="../index.html#work" class="back-link">&#8592; All Work</a>
    <div class="project-meta-row">
      <span class="project-cat mono">{p["catLabel"]}</span>
      <span class="section-num mono">SHEET {idx:02d}/{len(PROJECTS):02d}</span>
    </div>
    <h1 class="project-title">{p["title"]}</h1>
  </section>

  <section class="carousel wrap">
    <div class="carousel-frame" id="carouselFrame"></div>
    <span class="carousel-counter" id="carouselCounter"></span>
    <div class="carousel-thumbs" id="carouselThumbs"></div>
  </section>

  <section class="project-body wrap">
    <div>
      <p class="project-desc">{p["desc"]}</p>
    </div>
    <div class="project-side">
      <div class="side-block">
        <div class="side-label">Tools</div>
        <div class="chip-row">{tools_chips}</div>
      </div>
      <div class="side-block">
        <div class="side-label">Category</div>
        <div class="chip-row"><span class="chip">{p["catLabel"]}</span></div>
      </div>
    </div>
  </section>

  {FOOTER}
</main>

<script>
const PROJECT_TITLE = "{title_js}";
const PROJECT_SLUG = "{p["slug"]}";
</script>
<script src="../background.js" defer></script>
<script src="../carousel.js" defer></script>
</body>
</html>
"""
    out_path = os.path.join(PROJ_DIR, p["slug"] + ".html")
    with open(out_path, "w") as f:
        f.write(page)

print(f"{len(PROJECTS)} project pages written to /projects.")
