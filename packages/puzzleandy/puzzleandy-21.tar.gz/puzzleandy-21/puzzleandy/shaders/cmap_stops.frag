#version 330

struct ColStop
{
	float loc;
	vec3 col;
};

struct AlphaStop
{
	float loc;
	float alpha;
};

vec2 fragCoord = gl_FragCoord.xy;
uniform sampler2D iChannel0;
uniform vec3 iResolution;
uniform int num_col_stops;
uniform ColStop col_stops[10];
uniform float col_mids[9];
uniform int num_alpha_stops;
uniform AlphaStop alpha_stops[10];
uniform float alpha_mids[9];

out vec4 fragColor;

float unlerp(float fx, float f0, float f1)
{
	return (fx-f0)/(f1-f0);
}

void main()
{
	vec2 uv = fragCoord/iResolution.xy;
	float loc = texture(iChannel0, uv).r;
	vec3 col;
	float alpha;
	if (loc < col_stops[0].loc)
		col = col_stops[0].col;
	else if (loc > col_stops[num_col_stops-1].loc)
		col = col_stops[num_col_stops-1].col;
	else
	{
		int i;
		for (i = 0; i < num_col_stops; i++)
		{
			if (loc == col_stops[i].loc)
			{
				col = col_stops[i].col;
				break;
			}
		}
		if (i == num_col_stops)
		{
			for (int i = 0; i < num_col_stops-1; i++)
			{
				ColStop curr = col_stops[i];
				ColStop next = col_stops[i+1];
				if (curr.loc < loc && loc < next.loc)
				{
					float t = unlerp(loc,curr.loc,next.loc);
					float u = pow(t,log(0.5)/log(col_mids[i]));
					col = mix(curr.col,next.col,u);
					break;
				}
			}
		}
	}
	if (loc < alpha_stops[0].loc)
		alpha = alpha_stops[0].alpha;
	else if (loc > alpha_stops[num_alpha_stops-1].loc)
		alpha = alpha_stops[num_alpha_stops-1].alpha;
	else
	{
		int i;
		for (int i = 0; i < num_alpha_stops; i++)
		{
			if (loc == alpha_stops[i].loc)
			{
				alpha = alpha_stops[i].alpha;
				break;
			}
		}
		if (i == num_alpha_stops)
		{
			for (int i = 0; i < num_alpha_stops - 1; i++)
			{
				AlphaStop curr = alpha_stops[i];
				AlphaStop next = alpha_stops[i+1];
				if (curr.loc < loc && loc < next.loc)
				{
					float t = unlerp(loc, curr.loc, next.loc);
					float u = pow(t,log(0.5)/log(alpha_mids[i]));
					alpha = mix(curr.alpha,next.alpha,u);
					break;
				}
			}
		}
	}
	fragColor = vec4(col,alpha);
}