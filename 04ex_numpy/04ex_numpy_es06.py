positions = [0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448]
dis_grid = [[abs(positions[i]-positions[j]) for i in range(len(positions))]for j in range(len(positions))]
dis_grid = np.array(dis_grid)
print(dis_grid)