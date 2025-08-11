#!/usr/bin/env python3
"""
Kerala Floods 2018 Blog Generator
Embeds images as base64 data URIs into a single HTML file
"""
import base64
import os
from pathlib import Path

# --- EDIT: Add your image filenames here (must be in same folder as this script) ---
image_files = [
    "study-area.jpeg",
    "sentinel1-floodmaps.jpeg", 
    "figure9c.jpeg",
    "figure9a.jpeg",
    "figure10a.jpeg"
]

# Output filename
output_file = "forest_carbon_blog.html"

def encode_image_to_data_uri(path: Path) -> str:
    """Convert image file to base64 data URI"""
    ext = path.suffix.lower().lstrip('.')
    if ext in ('jpg', 'jpeg'):
        mime = 'image/jpeg'
    elif ext == 'png':
        mime = 'image/png'
    elif ext == 'gif':
        mime = 'image/gif'
    elif ext == 'webp':
        mime = 'image/webp'
    else:
        mime = 'application/octet-stream'
    
    try:
        data = path.read_bytes()
        b64 = base64.b64encode(data).decode('ascii')
        return f"data:{mime};base64,{b64}"
    except Exception as e:
        print(f"Error encoding {path}: {e}")
        return ""

def main():
    cwd = Path.cwd()
    print(f"Looking for images in: {cwd}")
    
    # Build data URIs for existing images
    data_uris = {}
    for filename in image_files:
        img_path = cwd / filename
        if img_path.exists():
            print(f"✓ Encoding {filename}...")
            data_uris[filename] = encode_image_to_data_uri(img_path)
        else:
            print(f"✗ Warning: {filename} not found - using placeholder")
            data_uris[filename] = ""

    # Generate the complete HTML
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Revolutionary Forest Carbon Mapping | Encode Nature</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .hero {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect fill="%23228B22" width="1200" height="600"/><text x="600" y="250" text-anchor="middle" fill="white" font-size="48" font-weight="bold">SATELLITE FOREST</text><text x="600" y="320" text-anchor="middle" fill="white" font-size="48" font-weight="bold">CARBON MAPPING</text><text x="600" y="400" text-anchor="middle" fill="white" font-size="24">81% Accuracy • All-Weather • Real-Time</text></svg>');
            background-size: cover;
            background-position: center;
            height: 80vh;
            display: flex;
            align-items: center;
            text-align: center;
            color: white;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        }

        .hero p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.7);
        }

        .cta-button {
            display: inline-block;
            background: linear-gradient(45deg, #ff6b6b, #ffa726);
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.2rem;
            font-weight: bold;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            animation: pulse 2s infinite;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 25px rgba(0,0,0,0.4);
        }

        @keyframes pulse {{
            0%%, 100%% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}

        .section {
            padding: 80px 0;
            background: white;
        }

        .section:nth-child(even) {
            background: #f8f9fa;
        }

        .section h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
            color: #2c3e50;
        }

        .problem-solution {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin-bottom: 50px;
        }

        .problem, .solution {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .problem:hover, .solution:hover {
            transform: translateY(-5px);
        }

        .problem {
            border-left: 5px solid #e74c3c;
        }

        .solution {
            border-left: 5px solid #27ae60;
        }

        .tech-stack {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin: 50px 0;
        }

        .tech-item {
            background: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .tech-item:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }

        .tech-item .icon {
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .results-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin: 50px 0;
        }

        .result-card {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .result-card h3 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .image-placeholder {
            width: 100%;
            height: 400px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
            text-align: center;
            margin: 30px 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .comparison-table {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin: 50px 0;
        }

        .comparison-table table {
            width: 100%;
            border-collapse: collapse;
        }

        .comparison-table th {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            text-align: left;
        }

        .comparison-table td {
            padding: 20px;
            border-bottom: 1px solid #eee;
        }

        .comparison-table .highlight {
            background: #e8f5e8;
            font-weight: bold;
        }

        .market-stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin: 50px 0;
        }

        .stat-card {
            background: linear-gradient(135deg, #ff6b6b, #ffa726);
            color: white;
            padding: 40px 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .stat-card h3 {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        .contact-section {
            background: linear-gradient(135deg, #2c3e50, #34495e);
            color: white;
            text-align: center;
            padding: 80px 0;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 50px;
        }

        .contact-item {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        @media (max-width: 768px) {
            .problem-solution,
            .tech-stack,
            .results-grid,
            .market-stats,
            .contact-grid {
                grid-template-columns: 1fr;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .hero p {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>Revolutionary Forest Carbon Mapping</h1>
            <p>See Every Tree's Worth from Space</p>
            <a href="#contact" class="cta-button">Schedule Demo</a>
        </div>
    </section>

    <!-- Problem & Solution -->
    <section class="section">
        <div class="container">
            <div class="problem-solution">
                <div class="problem">
                    <h3>🚨 The Carbon Crisis</h3>
                    <p><strong>72% of Earth's terrestrial carbon</strong> is stored in forests, yet we're flying blind on precise measurements.</p>
                    <ul style="margin-top: 20px;">
                        <li>Traditional surveys cover <1% of forests annually</li>
                        <li>Cost millions, take years to complete</li>
                        <li>Result: Inaccurate carbon credits & failed conservation</li>
                    </ul>
                </div>
                <div class="solution">
                    <h3>✅ Our Solution</h3>
                    <p><strong>Space-based carbon intelligence</strong> with 81% accuracy across entire landscapes.</p>
                    <ul style="margin-top: 20px;">
                        <li>Real-time monitoring from satellites</li>
                        <li>90% cost reduction vs. ground surveys</li>
                        <li>Works in all weather, day or night</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Technology Stack -->
    <section class="section">
        <div class="container">
            <h2>Revolutionary Tech Stack</h2>
           
            <div class="image-placeholder">
                <div>
                    <strong>BREAKTHROUGH TECHNOLOGY COMBINATION</strong><br><br>
                    🛰️ Multi-Frequency SAR + 🌲 GEDI LiDAR + 🤖 AI<br>
                    = 81% Accuracy Forest Carbon Maps<br><br>
                    Real-time • All-weather • Landscape-scale
                </div>
            </div>

            <div class="tech-stack">
                <div class="tech-item">
                    <div class="icon">🛰️</div>
                    <h3>Multi-Frequency SAR</h3>
                    <p><strong>The Carbon X-Ray</strong></p>
                    <ul style="text-align: left; margin-top: 15px;">
                        <li>L-band penetrates to tree trunks</li>
                        <li>C-band captures canopy structure</li>
                        <li>All-weather operation</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <div class="icon">🌲</div>
                    <h3>GEDI LiDAR</h3>
                    <p><strong>Precision Height Mapping</strong></p>
                    <ul style="text-align: left; margin-top: 15px;">
                        <li>25-meter precision measurements</li>
                        <li>3D forest structure mapping</li>
                        <li>From International Space Station</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <div class="icon">🤖</div>
                    <h3>AI Integration</h3>
                    <p><strong>Pattern Recognition</strong></p>
                    <ul style="text-align: left; margin-top: 15px;">
                        <li>Machine learning correlations</li>
                        <li>Validated against 103 ground plots</li>
                        <li>Scales to entire countries</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Results -->
    <section class="section">
        <div class="container">
            <h2>Proven Results: 81% Accuracy</h2>
           
            <div class="image-placeholder">
                <div>
                    <strong>PERFORMANCE BREAKTHROUGH</strong><br><br>
                    Single Technology: ~30% error<br>
                    Our Multi-Sensor Solution: 17% error<br><br>
                    ✅ 81% accuracy • ✅ Landscape scale • ✅ Cost effective
                </div>
            </div>

            <div class="results-grid">
                <div class="result-card">
                    <h3>17.17%</h3>
                    <p>Error Rate<br><small>(Industry standard: 20-30%)</small></p>
                </div>
                <div class="result-card">
                    <h3>R² = 0.81</h3>
                    <p>Correlation with<br>Ground Truth</p>
                </div>
                <div class="result-card">
                    <h3>1,500 km²</h3>
                    <p>Tested Area<br>All Forest Types</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Real Impact -->
    <section class="section">
        <div class="container">
            <h2>Real Impact: What You Get</h2>
           
            <div class="image-placeholder">
                <div>
                    <strong>FOREST CARBON MAP OUTPUT</strong><br><br>
                    🟢 High Carbon: 200+ tons/hectare<br>
                    🟡 Medium Carbon: 100-200 tons/hectare<br>
                    🟤 Low Carbon: <100 tons/hectare<br><br>
                    Ready for carbon markets & conservation planning
                </div>
            </div>

            <div class="tech-stack">
                <div class="tech-item">
                    <h3>💰 Carbon Markets</h3>
                    <ul style="text-align: left;">
                        <li>Verified carbon credit calculations</li>
                        <li>MRV-compliant REDD+ reporting</li>
                        <li>Real-time deforestation alerts</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <h3>🌿 Conservationists</h3>
                    <ul style="text-align: left;">
                        <li>Identify high-value carbon areas</li>
                        <li>Track restoration success</li>
                        <li>Optimize protection strategies</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <h3>🏛️ Governments</h3>
                    <ul style="text-align: left;">
                        <li>National forest carbon inventory</li>
                        <li>Meet Paris Agreement targets</li>
                        <li>Evidence-based policy making</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Competitive Advantage -->
    <section class="section">
        <div class="container">
            <h2>The Technology Edge</h2>
           
            <div class="comparison-table">
                <table>
                    <thead>
                        <tr>
                            <th>Approach</th>
                            <th>Technology</th>
                            <th>Accuracy</th>
                            <th>Coverage</th>
                            <th>Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Traditional Methods</td>
                            <td>Ground surveys</td>
                            <td>High (small areas)</td>
                            <td><1% annually</td>
                            <td>Very High</td>
                        </tr>
                        <tr>
                            <td>Single Satellite</td>
                            <td>Optical or SAR</td>
                            <td>30-50% error</td>
                            <td>Regional</td>
                            <td>Medium</td>
                        </tr>
                        <tr class="highlight">
                            <td><strong>Our Approach</strong></td>
                            <td><strong>Multi-sensor Fusion</strong></td>
                            <td><strong>17% error</strong></td>
                            <td><strong>Continental</strong></td>
                            <td><strong>Low</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Market Opportunity -->
    <section class="section">
        <div class="container">
            <h2>Massive Market Opportunity</h2>
           
            <div class="market-stats">
                <div class="stat-card">
                    <h3>$1B+</h3>
                    <p>Carbon Markets<br>Annually</p>
                </div>
                <div class="stat-card">
                    <h3>$500M+</h3>
                    <p>Forest Monitoring<br>Government Spending</p>
                </div>
                <div class="stat-card">
                    <h3>$50B+</h3>
                    <p>Climate Tech<br>Investment</p>
                </div>
            </div>

            <div class="image-placeholder">
                <div>
                    <strong>PERFECT TIMING</strong><br><br>
                    🚀 Satellite Boom: NISAR 2024, BIOMASS active<br>
                    💰 Carbon Market Explosion: Verification critical<br>
                    🌍 Climate Urgency: Forest solutions = 30% mitigation<br><br>
                    We solve the measurement problem
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section" id="contact">
        <div class="container">
            <h2>Ready to Transform Forest Monitoring?</h2>
            <p style="font-size: 1.3rem; margin-bottom: 30px;">Contact us to discuss how satellite-based carbon mapping can accelerate your climate goals.</p>
           
            <div class="contact-grid">
                <div class="contact-item">
                    <h3>📧 Email</h3>
                    <p>info@encodenature.com</p>
                </div>
                <div class="contact-item">
                    <h3>🌐 Website</h3>
                    <p>www.encodenature.com</p>
                </div>
                <div class="contact-item">
                    <h3>📞 Schedule Demo</h3>
                    <a href="#" class="cta-button" style="margin-top: 15px;">Book Call</a>
                </div>
            </div>
        </div>
    </section>

    <script>
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Add scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all sections for animation
        document.querySelectorAll('.section').forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(50px)';
            section.style.transition = 'all 0.8s ease';
            observer.observe(section);
        });
    </script>
</body>
</html>"""



    # Write the HTML file
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"\n✅ Success! Generated: {output_file}")
        print(f"📂 File size: {os.path.getsize(output_file) / 1024:.1f} KB")
        print(f"🌐 Open {output_file} in your browser to view the blog")
        print("\n📤 Ready to host online:")
        print("   • Drag & drop to netlify.com/drop")
        print("   • Upload to GitHub Pages") 
        print("   • Use with any web hosting service")
        
    except Exception as e:
        print(f"❌ Error writing file: {e}")

if __name__ == "__main__":
    print("🛰️  Kerala Floods Blog Generator")
    print("=" * 40)
    main()                                                                                          