from aligner import local_alignment, global_alignment

print('-----LOCAL-------')
local_alignment.initialize('CACTAT', 'AAT', 2, -2, -1)
local_alignment.calculate()
print('optimal alignment score: {}'.format(local_alignment.optimal_score()))
local_alignment.print_result()

print('-----GLOBAL------')
global_alignment.initialize('CACTAT', 'AAT', 2, -2, -1)
global_alignment.calculate()
print('optimal alignment score: {}'.format(global_alignment.optimal_score()))
global_alignment.print_result()
