"""
Car Dashboard Trim Removal Tool - 3D Model Generator
Creates an STL file for a pry tool that resembles a nail remover
Designed for 3D printing - strong and consistent
"""

import numpy as np
from stl import mesh
import math

def create_pry_tool():
    """
    Creates a car dashboard pry tool with:
    - Ergonomic handle
    - Flat wedge head
    - Forked end (like a nail remover)
    """
    
    vertices = []
    faces = []
    
    # ==========================================
    # DIMENSIONS (in mm)
    # ==========================================
    total_length = 180          # Total tool length
    handle_length = 100         # Handle section length
    handle_width = 25           # Handle width
    handle_height = 15          # Handle thickness
    
    head_length = 80            # Prying head length
    head_width_base = 25        # Width at base of head
    head_width_tip = 30         # Width at tip (forked)
    head_thickness_base = 8     # Thickness at base
    head_thickness_tip = 2      # Thin tip for prying
    
    fork_width = 8              # Width of fork slot
    fork_depth = 25             # How deep the fork goes
    
    # ==========================================
    # HANDLE SECTION (Ergonomic rounded shape)
    # ==========================================
    
    # Create handle vertices - tapered ergonomic shape
    handle_sections = 20
    for i in range(handle_sections + 1):
        t = i / handle_sections
        x = -handle_length * t
        
        # Ergonomic curve for grip
        grip_curve = math.sin(t * math.pi) * 0.3 + 1.0
        w = handle_width / 2 * grip_curve
        h = handle_height / 2 * grip_curve
        
        # Create octagonal cross-section for handle
        angles = [0, 45, 90, 135, 180, 225, 270, 315]
        for angle in angles:
            rad = math.radians(angle)
            y = w * math.cos(rad)
            z = h * math.sin(rad)
            vertices.append([x, y, z])
    
    # Connect handle sections with faces
    verts_per_section = 8
    for i in range(handle_sections):
        base = i * verts_per_section
        for j in range(verts_per_section):
            v1 = base + j
            v2 = base + (j + 1) % verts_per_section
            v3 = base + verts_per_section + j
            v4 = base + verts_per_section + (j + 1) % verts_per_section
            faces.append([v1, v2, v4])
            faces.append([v1, v4, v3])
    
    # Cap the back of handle
    handle_back_center = len(vertices)
    vertices.append([-handle_length, 0, 0])
    back_base = handle_sections * verts_per_section
    for j in range(verts_per_section):
        v1 = back_base + j
        v2 = back_base + (j + 1) % verts_per_section
        faces.append([handle_back_center, v2, v1])
    
    # ==========================================
    # HEAD SECTION (Wedge with fork)
    # ==========================================
    
    head_base_offset = len(vertices)
    head_sections = 15
    
    for i in range(head_sections + 1):
        t = i / head_sections
        x = head_length * t
        
        # Taper width and thickness towards tip
        w = head_width_base + (head_width_tip - head_width_base) * t
        h = head_thickness_base * (1 - t * 0.8)  # Thin towards tip
        
        # Create rectangular cross-section for head
        # But with fork cutout near the tip
        if t > 0.7:  # Fork starts at 70% of head length
            fork_t = (t - 0.7) / 0.3
            fork_w = fork_width / 2 * fork_t
            
            # Left prong
            vertices.append([x, -w/2, -h/2])
            vertices.append([x, -w/2, h/2])
            vertices.append([x, -fork_w, h/2])
            vertices.append([x, -fork_w, -h/2])
            
            # Right prong
            vertices.append([x, fork_w, -h/2])
            vertices.append([x, fork_w, h/2])
            vertices.append([x, w/2, h/2])
            vertices.append([x, w/2, -h/2])
        else:
            # Solid section
            vertices.append([x, -w/2, -h/2])
            vertices.append([x, -w/2, h/2])
            vertices.append([x, w/2, h/2])
            vertices.append([x, w/2, -h/2])
            # Duplicate for consistent vertex count
            vertices.append([x, -w/2, -h/2])
            vertices.append([x, -w/2, h/2])
            vertices.append([x, w/2, h/2])
            vertices.append([x, w/2, -h/2])
    
    # Connect head sections
    for i in range(head_sections):
        base = head_base_offset + i * 8
        for j in range(4):  # Only connect outer 4 vertices for now
            idx = [0, 1, 2, 3, 0][j:j+2]
            v1 = base + idx[0]
            v2 = base + idx[1]
            v3 = base + 8 + idx[0]
            v4 = base + 8 + idx[1]
            faces.append([v1, v2, v4])
            faces.append([v1, v4, v3])
    
    # Connect handle to head (transition section)
    # Front of handle connects to back of head
    handle_front_base = 0
    
    # Add transition vertices
    trans_offset = len(vertices)
    # Create smooth transition
    trans_w = handle_width / 2
    trans_h = handle_height / 2
    
    # Transition from octagonal handle to rectangular head
    vertices.append([0, -trans_w, -trans_h * 0.5])
    vertices.append([0, -trans_w, trans_h * 0.5])
    vertices.append([0, trans_w, trans_h * 0.5])
    vertices.append([0, trans_w, -trans_h * 0.5])
    
    # Connect to first handle section
    for j in range(verts_per_section):
        v1 = j
        v2 = (j + 1) % verts_per_section
        v3 = trans_offset + (j % 4)
        v4 = trans_offset + ((j + 1) % 4)
        faces.append([v1, v3, v2])
    
    # Connect to head
    for j in range(4):
        v1 = trans_offset + j
        v2 = trans_offset + (j + 1) % 4
        v3 = head_base_offset + j * 2
        v4 = head_base_offset + ((j + 1) % 4) * 2
        faces.append([v1, v2, v4])
        faces.append([v1, v4, v3])
    
    # Cap the tip (forked end)
    tip_base = head_base_offset + head_sections * 8
    
    # Left prong cap
    faces.append([tip_base + 0, tip_base + 1, tip_base + 2])
    faces.append([tip_base + 0, tip_base + 2, tip_base + 3])
    
    # Right prong cap
    faces.append([tip_base + 4, tip_base + 5, tip_base + 6])
    faces.append([tip_base + 4, tip_base + 6, tip_base + 7])
    
    return np.array(vertices), np.array(faces)


def create_simple_pry_tool():
    """
    Simplified version - creates a cleaner mesh
    """
    vertices = []
    faces = []
    
    # Dimensions in mm
    handle_length = 100
    head_length = 80
    handle_width = 22
    handle_height = 14
    head_width = 28
    head_tip_thickness = 2.5
    fork_width = 8
    fork_depth = 20
    
    # Create the tool as a series of cross-sections
    sections = []
    
    # Back of handle (rounded end)
    sections.append({
        'x': -handle_length,
        'points': create_rounded_rect(handle_width * 0.7, handle_height * 0.7, 8)
    })
    
    # Handle middle (grip area - thicker)
    for t in [0.2, 0.4, 0.5, 0.6, 0.8]:
        x = -handle_length * (1 - t)
        grip_factor = 1.0 + 0.15 * math.sin(t * math.pi)
        sections.append({
            'x': x,
            'points': create_rounded_rect(
                handle_width * grip_factor, 
                handle_height * grip_factor, 
                8
            )
        })
    
    # Handle front (transition to head)
    sections.append({
        'x': 0,
        'points': create_rounded_rect(handle_width, handle_height, 6)
    })
    
    # Head sections (tapering to thin wedge)
    for t in [0.1, 0.3, 0.5, 0.65]:
        x = head_length * t
        thickness = handle_height * (1 - t * 0.75)
        width = handle_width + (head_width - handle_width) * t
        sections.append({
            'x': x,
            'points': create_rounded_rect(width, thickness, 4)
        })
    
    # Fork start
    fork_start_x = head_length * 0.7
    fork_thickness = head_tip_thickness * 2
    sections.append({
        'x': fork_start_x,
        'points': create_forked_shape(head_width, fork_thickness, fork_width * 0.3)
    })
    
    # Fork middle
    sections.append({
        'x': head_length * 0.85,
        'points': create_forked_shape(head_width + 2, head_tip_thickness * 1.5, fork_width * 0.7)
    })
    
    # Fork tip
    sections.append({
        'x': head_length,
        'points': create_forked_shape(head_width + 4, head_tip_thickness, fork_width)
    })
    
    # Build vertices from sections
    vert_idx = 0
    section_starts = []
    
    for section in sections:
        section_starts.append(vert_idx)
        for y, z in section['points']:
            vertices.append([section['x'], y, z])
            vert_idx += 1
    
    # Create faces between sections
    for i in range(len(sections) - 1):
        n1 = len(sections[i]['points'])
        n2 = len(sections[i + 1]['points'])
        start1 = section_starts[i]
        start2 = section_starts[i + 1]
        
        # Simple case: same number of vertices
        if n1 == n2:
            for j in range(n1):
                v1 = start1 + j
                v2 = start1 + (j + 1) % n1
                v3 = start2 + j
                v4 = start2 + (j + 1) % n2
                faces.append([v1, v2, v4])
                faces.append([v1, v4, v3])
        else:
            # Use triangle fan for different vertex counts
            for j in range(max(n1, n2)):
                j1 = j % n1
                j2 = j % n2
                j1_next = (j + 1) % n1
                j2_next = (j + 1) % n2
                
                v1 = start1 + j1
                v2 = start1 + j1_next
                v3 = start2 + j2
                v4 = start2 + j2_next
                
                if j < n1 and j < n2:
                    faces.append([v1, v2, v4])
                    faces.append([v1, v4, v3])
    
    # Cap the ends
    # Back cap
    back_center = len(vertices)
    first_section = sections[0]['points']
    cx = sections[0]['x']
    vertices.append([cx, 0, 0])
    n = len(first_section)
    for j in range(n):
        faces.append([back_center, section_starts[0] + (j + 1) % n, section_starts[0] + j])
    
    # Front caps (left and right prongs)
    last_section = sections[-1]['points']
    last_start = section_starts[-1]
    n_last = len(last_section)
    tip_center = len(vertices)
    vertices.append([sections[-1]['x'], 0, 0])
    
    # Simple front cap
    mid = n_last // 2
    # Left half
    for j in range(mid - 1):
        faces.append([last_start + j, last_start + j + 1, tip_center])
    # Right half  
    for j in range(mid, n_last - 1):
        faces.append([last_start + j, last_start + j + 1, tip_center])
    
    return np.array(vertices, dtype=np.float64), faces


def create_rounded_rect(width, height, n_points):
    """Create a rounded rectangle cross-section"""
    points = []
    # Create points going around the rectangle
    hw = width / 2
    hh = height / 2
    
    for i in range(n_points):
        angle = 2 * math.pi * i / n_points
        # Superellipse for rounded rectangle effect
        y = hw * math.copysign(abs(math.cos(angle)) ** 0.7, math.cos(angle))
        z = hh * math.copysign(abs(math.sin(angle)) ** 0.7, math.sin(angle))
        points.append((y, z))
    
    return points


def create_forked_shape(width, height, fork_gap):
    """Create a forked cross-section (like a tuning fork)"""
    points = []
    hw = width / 2
    hh = height / 2
    fg = fork_gap / 2
    
    # Left prong outer edge
    points.append((-hw, -hh))
    points.append((-hw, hh))
    
    # Left prong inner edge
    points.append((-fg - 2, hh))
    points.append((-fg - 2, -hh))
    
    # Gap bottom (left side of gap)
    points.append((-fg, -hh))
    points.append((-fg, hh * 0.3))
    
    # Gap top
    points.append((fg, hh * 0.3))
    points.append((fg, -hh))
    
    # Right prong inner edge
    points.append((fg + 2, -hh))
    points.append((fg + 2, hh))
    
    # Right prong outer edge
    points.append((hw, hh))
    points.append((hw, -hh))
    
    return points


def create_solid_pry_tool():
    """
    Creates a solid, watertight mesh suitable for 3D printing
    Uses numpy-stl properly
    """
    # Tool dimensions (mm)
    handle_len = 100
    head_len = 80
    total_len = handle_len + head_len
    
    # Create arrays for the mesh
    all_vertices = []
    all_faces = []
    
    # Define cross-section profiles along the tool
    # Format: (x_position, width, height, is_forked, fork_gap)
    profiles = [
        (-handle_len, 18, 12, False, 0),        # Handle back
        (-handle_len * 0.8, 22, 14, False, 0),  # Handle grip start
        (-handle_len * 0.5, 24, 15, False, 0),  # Handle grip max
        (-handle_len * 0.2, 22, 14, False, 0),  # Handle grip end
        (0, 20, 12, False, 0),                   # Handle/head junction
        (head_len * 0.2, 22, 8, False, 0),      # Head start
        (head_len * 0.4, 25, 5, False, 0),      # Head middle
        (head_len * 0.6, 28, 4, False, 0),      # Head taper
        (head_len * 0.75, 30, 3, True, 4),      # Fork start
        (head_len * 0.9, 32, 2.5, True, 7),     # Fork middle
        (head_len, 34, 2, True, 10),            # Fork tip
    ]
    
    segments = 12  # Points per profile
    
    # Generate vertices for each profile
    profile_vertices = []
    for x, w, h, is_forked, fork_gap in profiles:
        profile_pts = []
        for i in range(segments):
            angle = 2 * math.pi * i / segments
            
            if is_forked and abs(math.cos(angle)) < 0.3 and math.sin(angle) < 0:
                # Create fork notch
                factor = 1 - (fork_gap / w) * (1 - abs(math.cos(angle)) / 0.3)
                y = (w / 2) * math.cos(angle) * max(0.3, factor)
            else:
                y = (w / 2) * math.cos(angle)
            
            z = (h / 2) * math.sin(angle)
            profile_pts.append([x, y, z])
        profile_vertices.append(profile_pts)
    
    # Flatten vertices
    for profile in profile_vertices:
        all_vertices.extend(profile)
    
    all_vertices = np.array(all_vertices)
    
    # Generate faces between profiles
    for p in range(len(profiles) - 1):
        base1 = p * segments
        base2 = (p + 1) * segments
        for i in range(segments):
            i_next = (i + 1) % segments
            # Two triangles per quad
            all_faces.append([base1 + i, base1 + i_next, base2 + i_next])
            all_faces.append([base1 + i, base2 + i_next, base2 + i])
    
    # Cap the back (handle end)
    back_center_idx = len(all_vertices)
    back_x = profiles[0][0]
    all_vertices = np.vstack([all_vertices, [[back_x, 0, 0]]])
    for i in range(segments):
        i_next = (i + 1) % segments
        all_faces.append([back_center_idx, i_next, i])
    
    # Cap the front (tip)
    front_center_idx = len(all_vertices)
    front_x = profiles[-1][0]
    all_vertices = np.vstack([all_vertices, [[front_x, 0, 0]]])
    front_base = (len(profiles) - 1) * segments
    for i in range(segments):
        i_next = (i + 1) % segments
        all_faces.append([front_center_idx, front_base + i, front_base + i_next])
    
    all_faces = np.array(all_faces)
    
    return all_vertices, all_faces


def generate_stl(filename="dashboard_pry_tool.stl"):
    """Generate and save the STL file"""
    print("Generating 3D model of Dashboard Pry Tool...")
    
    vertices, faces = create_solid_pry_tool()
    
    print(f"Created {len(vertices)} vertices and {len(faces)} faces")
    
    # Create the mesh
    tool_mesh = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    
    for i, face in enumerate(faces):
        for j in range(3):
            tool_mesh.vectors[i][j] = vertices[face[j]]
    
    # Save to file
    tool_mesh.save(filename)
    print(f"STL file saved as: {filename}")
    
    # Print some stats
    volume, cog, inertia = tool_mesh.get_mass_properties()
    print(f"\nModel Statistics:")
    print(f"  Volume: {abs(volume):.2f} mm³")
    print(f"  Center of gravity: ({cog[0]:.1f}, {cog[1]:.1f}, {cog[2]:.1f}) mm")
    print(f"  Bounding box: X={vertices[:,0].min():.1f} to {vertices[:,0].max():.1f} mm")
    print(f"                Y={vertices[:,1].min():.1f} to {vertices[:,1].max():.1f} mm")  
    print(f"                Z={vertices[:,2].min():.1f} to {vertices[:,2].max():.1f} mm")
    
    total_length = vertices[:,0].max() - vertices[:,0].min()
    max_width = vertices[:,1].max() - vertices[:,1].min()
    max_height = vertices[:,2].max() - vertices[:,2].min()
    print(f"\n  Total length: {total_length:.1f} mm")
    print(f"  Max width: {max_width:.1f} mm")
    print(f"  Max height: {max_height:.1f} mm")
    
    return filename


if __name__ == "__main__":
    generate_stl("dashboard_pry_tool.stl")
    print("\n✅ Done! You can now 3D print the tool.")
    print("\nRecommended print settings:")
    print("  - Material: PETG or ABS for durability")
    print("  - Infill: 60-80% for strength")
    print("  - Layer height: 0.2mm")
    print("  - Orientation: Flat on build plate")
